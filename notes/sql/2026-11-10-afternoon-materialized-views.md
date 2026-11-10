# Materialized Views

**Category:** SQL  
**Date:** 2026-11-10 (afternoon)

---

# Materialized Views

A **materialized view** is a database object that stores the result set of a query physically, unlike a regular view which runs the underlying query each time it is referenced. The stored data can be refreshed on demand, on a schedule, or automatically when the base tables change (if the DBMS supports incremental refresh).

**Why use it?**  
- **Performance:** Queries that involve heavy aggregations, joins across large tables, or complex calculations can be answered instantly from the pre‑computed result, reducing CPU and I/O load.  
- **Data Warehousing:** Frequently accessed reporting snapshots (e.g., daily sales totals) are ideal candidates.  
- **Isolation:** Consumers can query a stable snapshot while the source tables continue to be updated, avoiding locking conflicts.

**Typical usage pattern**

```sql
-- 1. Create a materialized view
CREATE MATERIALIZED VIEW mv_monthly_sales AS
SELECT
    store_id,
    DATE_TRUNC('month', sale_date) AS month,
    SUM(amount) AS total_sales
FROM sales
GROUP BY store_id, DATE_TRUNC('month', sale_date);

-- 2. Refresh it manually (full refresh)
REFRESH MATERIALIZED VIEW mv_monthly_sales;

-- 3. Or schedule incremental refresh (PostgreSQL example)
CREATE EXTENSION IF NOT EXISTS pg_cron;
SELECT cron.schedule('0 2 * * *',
    $$REFRESH MATERIALIZED VIEW CONCURRENTLY mv_monthly_sales$$);
```

When a **CONCURRENTLY** refresh is supported, the view remains queryable during the refresh, at the cost of a slightly longer refresh time.

**When to avoid:**  
If the underlying data changes constantly and near‑real‑time accuracy is required, the overhead of frequent refreshes may outweigh the performance gains.

---
