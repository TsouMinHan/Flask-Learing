from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # 因為資料庫連線問題才會進到這邊，所以回朔資料庫
    return render_template('500.html'), 500
