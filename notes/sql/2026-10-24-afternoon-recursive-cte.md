# Recursive CTE

**Category:** SQL  
**Date:** 2026-10-24 (afternoon)

---

# Recursive CTE (Common Table Expression)

A **recursive CTE** lets a query reference its own output, enabling you to walk hierarchical or graph‑like data directly in SQL. It consists of two parts: an *anchor* query that returns the root rows, and a *recursive* query that repeatedly joins the CTE to its child rows until no new rows appear. The engine automatically handles the iteration, stopping when the result set stops growing (or when a `MAXRECURSION` limit is hit).

**Why use it?**  
- Traversing organizational charts, category trees, bill‑of‑materials, or folder structures without needing procedural code.  
- Generating sequences (e.g., dates, numbers) on the fly.  
- Solving graph problems such as finding paths or detecting cycles, all within a single SQL statement.

**Example – Employee hierarchy**

```sql
-- Employees table: id, name, manager_id (NULL for top boss)
WITH RECURSIVE OrgChart AS (
    -- Anchor: top‑level manager(s)
    SELECT id, name, manager_id, 1 AS lvl, CAST(name AS VARCHAR(200)) AS path
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive step: attach direct reports
    SELECT e.id, e.name, e.manager_id, oc.lvl + 1,
           CONCAT(oc.path, ' > ', e.name)
    FROM Employees e
    JOIN OrgChart oc ON e.manager_id = oc.id
)
SELECT id, name, manager_id, lvl, path
FROM OrgChart
ORDER BY lvl, name;
```

The query builds a tree, assigning each employee a level (`lvl`) and a breadcrumb‑style `path`. Recursive CTEs are ANSI‑SQL standard and work in PostgreSQL, SQL Server, MySQL 8+, Oracle, and SQLite (with `WITH RECURSIVE`). They are a powerful, set‑based alternative to looping logic in application code.
