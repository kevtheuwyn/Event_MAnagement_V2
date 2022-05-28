from flask import Blueprint,render_template,url_for,redirect

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return '<h1>Starter code for the assessment<h1>'
    # render_template('templates/accounts/login.html')