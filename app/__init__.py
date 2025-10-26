from flask import Flask, g
from .app_factory import create_app
from .db_connect import close_db, get_db

app = create_app()
app.secret_key = 'your-secret'  # Replace with an environment
app.config['SESSION_PERMANENT'] = False  # Session expires when browser closes
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes if permanent session

# Register Blueprints
from app.blueprints.auth import auth
from app.blueprints.menu import menu
from app.blueprints.customers import customers
from app.blueprints.orders import orders

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(menu, url_prefix='/menu')
app.register_blueprint(customers, url_prefix='/customers')
app.register_blueprint(orders, url_prefix='/orders')

from . import routes

@app.before_request
def before_request():
    g.db = get_db()
    if g.db is None:
        print("Warning: Database connection unavailable. Some features may not work.")

@app.after_request
def add_header(response):
    """Add headers to prevent caching of protected pages"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)