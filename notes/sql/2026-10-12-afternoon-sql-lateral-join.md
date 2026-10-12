# SQL Lateral Join

**Category:** SQL  
**Date:** 2026-10-12 (afternoon)

---

# SQL Lateral Join

A **LATERAL** join (known as `CROSS APPLY` in SQL Server) lets a subquery reference columns from a preceding table expression in the same `FROM` clause. The subquery is evaluated **per row** of the left‑hand table, producing a result set that can be joined back to that row. This enables row‑by‑row calculations, correlated table‑valued functions, or limiting results per group without resorting to complex window functions.

### When to use it
- **Top‑N per group**: Quickly fetch the first few rows for each category.
- **JSON / XML extraction**: Apply a JSON‑parsing function to each row’s column.
- **Dynamic joins**: Join to a table‑valued function that depends on a column’s value.
- **Simplify correlated subqueries**: Improves readability and often yields better execution plans.

### Example (PostgreSQL)

```sql
-- Get the three most recent orders for each customer
SELECT c.customer_id,
       o.order_id,
       o.order_date
FROM   customers c
CROSS JOIN LATERAL (
        SELECT order_id, order_date
        FROM   orders o
        WHERE  o.customer_id = c.customer_id
        ORDER BY o.order_date DESC
        LIMIT 3
) AS o;
```

In this query, the inner sub‑select runs for each `customers` row, returning up to three of that customer's latest orders. The result behaves like a regular join but avoids the need for window functions such as `ROW_NUMBER()`.

**Key take‑away:** LATERAL joins empower you to treat a row‑wise subquery as a table, opening flexible, performant patterns for per‑row processing.
