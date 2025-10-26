from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.db_connect import get_db
from functools import wraps

auth = Blueprint('auth', __name__)

def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@auth.route('/logout')
def logout():
    # Get username before clearing session
    username = session.get('full_name', 'User')

    # Clear session
    session.clear()

    flash(f'Goodbye, {username}! You have been logged out.', 'success')
    return redirect(url_for('index'))
