SELECT
    customer_id,
    order_date,
    price,
    ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date
	) AS order_rank
FROM sales
-- ORDER BY customer_id desc
;

SELECT
    category,
    price,
    RANK() OVER(PARTITION BY category ORDER BY price DESC) AS price_rank
FROM sales;

SELECT
    customer_id,
    order_date,
    price,
    LAG(price,1,0) OVER(PARTITION BY customer_id ORDER BY order_date) AS previous_price
FROM sales;

