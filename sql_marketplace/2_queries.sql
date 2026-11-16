-- =========================================================================
-- E-commerce Marketplace Analytics Queries
-- Author: Aliaksandra Yushkis-Radziuk
-- Description: Analytical SQL queries demonstrating multi-table joins, 
--              aggregations, filtering, and data grouping.
-- =========================================================================


-- QUERY 1: Calculate total revenue and sold items per seller
-- Skills demonstrated: INNER JOIN, GROUP BY, Aggregate functions (SUM, COUNT), ORDER BY
SELECT 
    u.username,
    COUNT(i.item_id) AS total_sold_items,
    SUM(i.price) AS total_revenue
FROM users u
JOIN items i ON u.user_id = i.seller_id
WHERE i.status = 'sold'
GROUP BY u.username
ORDER BY total_revenue DESC;


-- QUERY 2: Find the average price of sold items grouped by category
-- Skills demonstrated: Filtering (WHERE), Aggregation (COUNT, AVG), Rounding, GROUP BY
SELECT 
    category,
    COUNT(item_id) AS items_count,
    ROUND(AVG(price), 2) AS avg_price
FROM items
WHERE status = 'sold'
GROUP BY category;


-- QUERY 3: Retrieve top-3 most expensive active listings on the platform
-- Skills demonstrated: Data filtering, Sorting (ORDER BY DESC), and Result restriction (LIMIT)
SELECT 
    title,
    category,
    price
FROM items
WHERE status = 'active'
ORDER BY price DESC
LIMIT 3;