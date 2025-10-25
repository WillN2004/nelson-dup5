from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

menu = Blueprint('menu', __name__)

@menu.route('/', methods=['GET', 'POST'])
def show_menu():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new menu item
    if request.method == 'POST':
        name = request.form['name']
        size = request.form['size']
        price = request.form['price']
        cost = request.form['cost']

        # Insert the new menu item into the database
        cursor.execute('INSERT INTO menu_items (name, size, price, cost) VALUES (%s, %s, %s, %s)',
                       (name, size, price, cost))
        db.commit()

        flash('New menu item added successfully!', 'success')
        return redirect(url_for('menu.show_menu'))

    # Handle GET request to display all menu items
    cursor.execute('SELECT * FROM menu_items')
    all_menu_items = cursor.fetchall()
    return render_template('menu.html', all_menu_items=all_menu_items)

@menu.route('/update_menu/<int:item_id>', methods=['POST'])
def update_menu(item_id):
    db = get_db()
    cursor = db.cursor()

    # Update the menu item's details
    name = request.form['name']
    size = request.form['size']
    price = request.form['price']
    cost = request.form['cost']

    cursor.execute('UPDATE menu_items SET name = %s, size = %s, price = %s, cost = %s WHERE item_id = %s',
                   (name, size, price, cost, item_id))
    db.commit()

    flash('Menu item updated successfully!', 'success')
    return redirect(url_for('menu.show_menu'))

@menu.route('/delete_menu/<int:item_id>', methods=['POST'])
def delete_menu(item_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the menu item
    cursor.execute('DELETE FROM menu_items WHERE item_id = %s', (item_id,))
    db.commit()

    flash('Menu item deleted successfully!', 'danger')
    return redirect(url_for('menu.show_menu'))
