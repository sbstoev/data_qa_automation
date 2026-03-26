
WITH customer_spending AS (
    SELECT
        customer_id,
        SUM(price*quantity) AS total_spent
    FROM sales
    GROUP BY customer_id
)

SELECT *
FROM customer_spending
-- WHERE total_spent > 500
ORDER BY 1
;
