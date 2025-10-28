from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db
from app.blueprints.auth import login_required

orders = Blueprint('orders', __name__)

@orders.route('/', methods=['GET', 'POST'])
@login_required
def show_orders():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new order
    if request.method == 'POST':
        customer_id = request.form['customer']

        # Insert the new order into the database
        cursor.execute('INSERT INTO `order` (customer) VALUES (%s)', (customer_id,))
        db.commit()

        order_id = cursor.lastrowid

        flash(f'New order #{order_id} created successfully!', 'success')
        return redirect(url_for('orders.show_orders'))

    # Get all orders with customer information
    cursor.execute('''
        SELECT o.order_id, o.customer, o.date, c.name as customer_name
        FROM `order` o
        JOIN customer c ON o.customer = c.customer_id
        ORDER BY o.date DESC
    ''')
    all_orders = cursor.fetchall()

    # Get all non-archived customers for dropdown
    cursor.execute('SELECT customer_id, name FROM customer WHERE archived = FALSE')
    all_customers = cursor.fetchall()

    # Get order details for each order
    order_details = {}
    for order in all_orders:
        cursor.execute('''
            SELECT od.order_detail_id, od.order_id, od.item_id, od.quantity,
                   mi.name as item_name, mi.size, mi.price
            FROM order_detail od
            JOIN menu_items mi ON od.item_id = mi.item_id
            WHERE od.order_id = %s
        ''', (order['order_id'],))
        order_details[order['order_id']] = cursor.fetchall()

    # Get all menu items for dropdown
    cursor.execute('SELECT item_id, name, size, price FROM menu_items')
    all_menu_items = cursor.fetchall()

    return render_template('orders.html',
                         all_orders=all_orders,
                         all_customers=all_customers,
                         order_details=order_details,
                         all_menu_items=all_menu_items)

@orders.route('/delete_order/<int:order_id>', methods=['POST'])
@login_required
def delete_order(order_id):
    db = get_db()
    cursor = db.cursor()

    # Delete order details first (foreign key constraint)
    cursor.execute('DELETE FROM order_detail WHERE order_id = %s', (order_id,))

    # Delete the order
    cursor.execute('DELETE FROM `order` WHERE order_id = %s', (order_id,))
    db.commit()

    flash('Order deleted successfully!', 'danger')
    return redirect(url_for('orders.show_orders'))

@orders.route('/add_order_detail/<int:order_id>', methods=['POST'])
@login_required
def add_order_detail(order_id):
    db = get_db()
    cursor = db.cursor()

    item_id = request.form['item_id']
    quantity = request.form['quantity']

    # Insert the new order detail
    cursor.execute('INSERT INTO order_detail (order_id, item_id, quantity) VALUES (%s, %s, %s)',
                   (order_id, item_id, quantity))
    db.commit()

    flash('Item added to order successfully!', 'success')
    return redirect(url_for('orders.show_orders'))

@orders.route('/update_order_detail/<int:order_detail_id>', methods=['POST'])
@login_required
def update_order_detail(order_detail_id):
    db = get_db()
    cursor = db.cursor()

    item_id = request.form['item_id']
    quantity = request.form['quantity']

    cursor.execute('UPDATE order_detail SET item_id = %s, quantity = %s WHERE order_detail_id = %s',
                   (item_id, quantity, order_detail_id))
    db.commit()

    flash('Order item updated successfully!', 'success')
    return redirect(url_for('orders.show_orders'))

@orders.route('/delete_order_detail/<int:order_detail_id>', methods=['POST'])
@login_required
def delete_order_detail(order_detail_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute('DELETE FROM order_detail WHERE order_detail_id = %s', (order_detail_id,))
    db.commit()

    flash('Order item removed successfully!', 'danger')
    return redirect(url_for('orders.show_orders'))
