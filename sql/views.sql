CREATE OR REPLACE VIEW vw_sales_analysis AS
SELECT
    oi.order_item_id,
    o.order_id,
    o.order_date,
    o.status,

    c.customer_id,
    c.name AS customer_name,
    c.city,
    c.state,

    p.product_id,
    p.product_name,
    p.category,

    oi.quantity,
    oi.unit_price,

    oi.quantity * oi.unit_price AS total_price,

    CASE
        WHEN o.status = 'completed'
        THEN oi.quantity * oi.unit_price
        ELSE 0
    END AS effective_revenue

FROM order_items oi

JOIN orders o
    ON oi.order_id = o.order_id

JOIN customers c
    ON o.customer_id = c.customer_id

JOIN products p
    ON oi.product_id = p.product_id;