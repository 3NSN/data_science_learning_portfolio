
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    country VARCHAR(30) NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    seller_id INT REFERENCES users(user_id),
    title VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'sold', 'reserved'))
);

INSERT INTO users (username, country, created_at) VALUES
('anna_vinted', 'Lithuania', '2025-01-15'),
('marius_lt', 'Lithuania', '2025-03-20'),
('elena_shop', 'Latvia', '2025-06-10'),
('tomas_k', 'Estonia', '2025-08-01');

INSERT INTO items (seller_id, title, category, price, status) VALUES
(1, 'Vintage Levi''s Jeans', 'Clothing', 35.00, 'sold'),
(1, 'Nike Air Max Sneakers', 'Shoes', 60.00, 'active'),
(2, 'Wool Winter Coat', 'Clothing', 85.00, 'sold'),
(3, 'Leather Backpack', 'Accessories', 45.00, 'active'),
(3, 'Silver Ring', 'Jewelry', 20.00, 'sold'),
(4, 'Board Game Set', 'Toys', 25.00, 'active'),
(1, 'Summer Floral Dress', 'Clothing', 25.00, 'sold');