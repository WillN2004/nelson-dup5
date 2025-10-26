-- Sample data for Will's Coffee Shop
-- Run this after creating the schema to populate with sample records

-- Insert sample customers
INSERT INTO customer (name, phone, email) VALUES
('Emily Rodriguez', '555-0101', 'emily.r@email.com'),
('James Chen', '555-0102', 'james.chen@email.com'),
('Sarah Mitchell', '555-0103', 'sarah.mitchell@email.com'),
('Michael O''Connor', '555-0104', 'michael.oconnor@email.com'),
('Amanda Thompson', '555-0105', 'amanda.t@email.com'),
('David Kim', '555-0106', 'david.kim@email.com'),
('Jessica Martinez', '555-0107', 'jessica.m@email.com'),
('Ryan Parker', '555-0108', 'ryan.parker@email.com');

-- Insert sample menu items - Coffee Drinks
INSERT INTO menu_items (name, size, price, cost) VALUES
('Espresso', 'Single', 2.95, 0.75),
('Espresso', 'Double', 3.95, 1.25),
('Americano', 'Small', 3.25, 0.85),
('Americano', 'Medium', 3.95, 1.15),
('Americano', 'Large', 4.65, 1.45),
('Latte', 'Small', 4.25, 1.25),
('Latte', 'Medium', 4.95, 1.65),
('Latte', 'Large', 5.65, 2.05),
('Cappuccino', 'Small', 4.25, 1.25),
('Cappuccino', 'Medium', 4.95, 1.65),
('Cappuccino', 'Large', 5.65, 2.05),
('Mocha', 'Small', 4.75, 1.55),
('Mocha', 'Medium', 5.45, 1.95),
('Mocha', 'Large', 6.15, 2.35),
('Caramel Macchiato', 'Small', 4.95, 1.65),
('Caramel Macchiato', 'Medium', 5.65, 2.05),
('Caramel Macchiato', 'Large', 6.35, 2.45),
('Cold Brew', 'Small', 3.95, 1.15),
('Cold Brew', 'Medium', 4.65, 1.55),
('Cold Brew', 'Large', 5.35, 1.95),
('Iced Latte', 'Medium', 4.95, 1.65),
('Iced Latte', 'Large', 5.65, 2.05),
('Vanilla Latte', 'Small', 4.75, 1.55),
('Vanilla Latte', 'Medium', 5.45, 1.95),
('Vanilla Latte', 'Large', 6.15, 2.35);

-- Insert pastries and food items
INSERT INTO menu_items (name, size, price, cost) VALUES
('Croissant', 'Regular', 3.95, 1.25),
('Chocolate Croissant', 'Regular', 4.25, 1.45),
('Blueberry Muffin', 'Regular', 3.75, 1.15),
('Banana Nut Muffin', 'Regular', 3.75, 1.15),
('Cinnamon Roll', 'Regular', 4.50, 1.65),
('Bagel with Cream Cheese', 'Regular', 3.95, 1.05),
('Avocado Toast', 'Regular', 7.95, 3.25),
('Breakfast Sandwich', 'Regular', 6.95, 2.85),
('Granola Parfait', 'Regular', 5.95, 2.45),
('Cookie', 'Regular', 2.95, 0.85),
('Brownie', 'Regular', 3.95, 1.25);

-- Insert sample employees
INSERT INTO employee (fname, lname, password, username) VALUES
('Admin', 'User', 'hashed_password_1', 'willnelson'),
('Emma', 'Davis', 'hashed_password_2', 'edavis'),
('Lucas', 'Anderson', 'hashed_password_3', 'landerson'),
('Olivia', 'Taylor', 'hashed_password_4', 'otaylor');

-- Insert sample orders
INSERT INTO `order` (customer, date) VALUES
(1, '2025-10-23 08:15:00'),
(2, '2025-10-23 09:30:00'),
(3, '2025-10-23 10:45:00'),
(4, '2025-10-24 07:30:00'),
(5, '2025-10-24 11:20:00'),
(1, '2025-10-24 14:15:00'),
(6, '2025-10-25 08:00:00'),
(7, '2025-10-25 09:15:00');

-- Insert sample order details
INSERT INTO order_detail (order_id, item_id, quantity) VALUES
(1, 7, 1),
(1, 26, 1),
(2, 2, 2),
(2, 30, 1),
(3, 15, 1),
(3, 27, 1),
(3, 35, 1),
(4, 4, 1),
(4, 32, 1),
(5, 21, 1),
(5, 33, 1),
(5, 36, 2),
(6, 13, 1),
(6, 28, 1),
(7, 8, 1),
(7, 29, 1),
(8, 20, 1),
(8, 31, 1);