-- Database Schema for Flask Starter Kit
-- Run this file to create the required database structure

-- Create customer table
CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    archived BOOLEAN DEFAULT FALSE
);

-- Create menu_items table
CREATE TABLE menu_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    size VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL
);

-- Create employee table
CREATE TABLE employee (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE
);

-- Create order table
CREATE TABLE `order` (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer INT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer) REFERENCES customer(customer_id)
);

-- Create order_detail table
CREATE TABLE order_detail (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES `order`(order_id),
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);

-- Add indexes for common queries
CREATE INDEX idx_customer_email ON customer (email);
CREATE INDEX idx_employee_username ON employee (username);
CREATE INDEX idx_order_customer ON `order` (customer);
CREATE INDEX idx_order_date ON `order` (date);
CREATE INDEX idx_order_detail_order ON order_detail (order_id);
CREATE INDEX idx_order_detail_item ON order_detail (item_id);