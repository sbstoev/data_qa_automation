SELECT
    customer_id,
    order_date,
    price,
    ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_rank
FROM sales;
