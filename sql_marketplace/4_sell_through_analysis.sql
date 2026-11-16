-- Synthetic data only. Category differences are deliberately constructed;
-- these results do not represent real Vinted performance.

-- 1. Count listings in each category and status.
SELECT category, status, COUNT(*) AS listings
FROM demo_items
GROUP BY category, status
ORDER BY category, status;

-- 2. Sold share in a single snapshot, not 30-day sell-through.
-- All statuses (active, sold, reserved) stay in the denominator.
-- Only sold counts as a sale; 100.0 avoids integer division.
SELECT
    category,
    COUNT(*) AS total_listings,
    SUM(CASE WHEN status = 'sold' THEN 1 ELSE 0 END) AS sold_listings,
    ROUND(100.0 * SUM(CASE WHEN status = 'sold' THEN 1 ELSE 0 END)
          / COUNT(*), 2) AS sold_percentage
FROM demo_items
GROUP BY category
ORDER BY category;

-- 3. Average listed price of sold items (EUR).
-- Actual transaction amounts are unavailable.
SELECT
    category,
    ROUND(AVG(price), 2) AS average_listed_price_of_sold_items
FROM demo_items
WHERE status = 'sold'
GROUP BY category
ORDER BY category;
