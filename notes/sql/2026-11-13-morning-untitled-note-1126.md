# Untitled Note - 1126

**Category:** SQL  
**Date:** 2026-11-13 (morning)

---

# Temporary Tables

Temporary tables are session‑scoped objects that exist only for the duration of a database connection (or transaction). They are created with `CREATE TEMPORARY TABLE` (MySQL, PostgreSQL) or `CREATE TABLE #temp` (SQL Server). Because they are stored in temp space, they avoid locking the base tables and can be indexed, allowing complex intermediate calculations without affecting the production schema.

**Why use them?**  
- **Staging data** for multi‑step ETL pipelines.  
- **Breaking down** large queries into manageable parts, improving readability and sometimes performance.  
- **Isolating** work in a session so concurrent users don’t see the interim results.  
- **Reducing I/O**: many RDBMS keep temp tables in memory or a fast temp file system.

**Example (PostgreSQL)**  

```sql
BEGIN;

-- Load a subset of orders into a temporary table
CREATE TEMPORARY TABLE tmp_orders AS
SELECT order_id, customer_id, total
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days';

-- Index the temp table for faster joins
CREATE INDEX idx_tmp_orders_customer ON tmp_orders(customer_id);

-- Use the temp table in a join
SELECT c.customer_name, SUM(t.total) AS month_total
FROM customers c
JOIN tmp_orders t ON c.customer_id = t.customer_id
GROUP BY c.customer_name
ORDER BY month_total DESC;

COMMIT;   -- Temp table disappears automatically
```

When the session ends or the transaction commits (depending on the DBMS), the temporary table is dropped automatically, leaving no trace in the permanent schema.

SUBTOP
