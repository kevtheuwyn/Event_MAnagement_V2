from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required,logout_user


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
# @login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        'home/index.html',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!"
    )

@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

@main_bp.route('/creation', methods=['GET','POST'])
# @login_required
def createEvent():
    """Logged-in User Dashboard."""
    return render_template(
        'home/creation.html',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!"
    )

@main_bp.route('/history', methods=['GET','POST'])
# @login_required
def history():
    """Logged-in User Dashboard."""
    return render_template(
        'home/book_history.html',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!"
    )

@main_bp.route('/details', methods=['GET','POST'])
# @login_required
def event_details():
    """Logged-in User Dashboard."""
    return render_template(
        'home/event_details.html',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
    )