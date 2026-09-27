# Suggested Screenshot Checklist

Use this list while executing the workshop.

1. Python, MySQL, SQLAlchemy and FastAPI versions.
2. `SHOW TABLES;` displaying:
   - customers
   - orders
   - order_items
   - products
3. Customer creation or update using curl.
4. Corresponding customer data in MySQL.
5. Product creation or update using curl.
6. Corresponding product data in MySQL.
7. `SELECT * FROM orders;`
8. `SELECT * FROM order_items;`
9. Nested JSON from `GET /orders/{order_id}`.
10. SQLAlchemy/Uvicorn output showing the generated `UPDATE`.
11. Before and after cascade-delete evidence:
    - orders
    - order_items
    - products
12. Product inventory before a successful transaction.
13. Product inventory after a successful transaction.
14. Failed transaction with:
    `Insufficient stock for Webcam`
15. Inventory after rollback proving Product 1 was not reduced.
16. Python client menu.
17. Successful client operation.
18. Final endpoint:
    `GET /products/1/customers`
