from flask import render_template, redirect, url_for, session, request, flash
from . import app
from app.blueprints.auth import login_required
from app.db_connect import get_db

@app.route('/', methods=['GET', 'POST'])
def index():
    # If already logged in, redirect to dashboard
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    # Handle login on index page
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()

        # Query employee by username
        cursor.execute('SELECT user_id, fname, lname, password, username FROM employee WHERE username = %s', (username,))
        user = cursor.fetchone()

        # Check if user exists and password matches
        if user and user['password'] == password:
            # Store user info in session
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['full_name'] = f"{user['fname']} {user['lname']}"

            flash(f'Welcome back, {user["fname"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            return redirect(url_for('index'))

    # Show index/login page
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    cursor = db.cursor()

    # Get total sales for current year
    cursor.execute('''
        SELECT COALESCE(SUM(mi.price), 0) as total_sales
        FROM `order` o
        JOIN order_detail od ON o.order_id = od.order_id
        JOIN menu_items mi ON od.item_id = mi.item_id
        WHERE YEAR(o.date) = YEAR(CURDATE())
    ''')
    total_sales = cursor.fetchone()['total_sales']

    # Get total number of customers
    cursor.execute('SELECT COUNT(*) as customer_count FROM customer')
    customer_count = cursor.fetchone()['customer_count']

    # Get 5 most recent orders
    cursor.execute('''
        SELECT
            o.order_id,
            c.name as customer_name,
            o.date as order_date,
            COUNT(od.item_id) as item_count,
            SUM(mi.price) as total_amount
        FROM `order` o
        JOIN customer c ON o.customer = c.customer_id
        JOIN order_detail od ON o.order_id = od.order_id
        JOIN menu_items mi ON od.item_id = mi.item_id
        GROUP BY o.order_id, c.name, o.date
        ORDER BY o.date DESC
        LIMIT 5
    ''')
    recent_orders = cursor.fetchall()

    return render_template('dashboard.html',
                         total_sales=total_sales,
                         customer_count=customer_count,
                         recent_orders=recent_orders)

@app.route('/about')
def about():
    return render_template('about.html')
