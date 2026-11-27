# Filtered Indexes

**Category:** SQL  
**Date:** 2026-11-27 (afternoon)

---

# Filtered Indexes

A **filtered index** is a non‑clustered index that includes only a subset of rows in a table, defined by a `WHERE` predicate. Unlike a regular index that indexes every row, the filtered version stores entries only for rows that satisfy the filter condition, making it smaller and faster to maintain.

### Why use it?
- **Performance boost** for queries that frequently access a specific slice of data (e.g., active rows, recent dates).
- **Reduced storage** and I/O because the index size matches only the filtered rows.
- **Improved write throughput**: fewer index updates on inserts/updates that don’t meet the filter.
- Ideal for **sparse data** patterns, such as soft‑deleted records (`IsDeleted = 0`) or columns that are mostly `NULL`.

### Practical example (SQL Server)

```sql
-- Table with many rows, only a few are active
CREATE TABLE Orders (
    OrderID int PRIMARY KEY,
    CustomerID int,
    OrderDate datetime,
    IsProcessed bit
);

-- Filtered index for only unprocessed orders
CREATE NONCLUSTERED INDEX IX_Orders_Unprocessed
ON Orders (OrderDate)
WHERE IsProcessed = 0;
```

When the query `SELECT * FROM Orders WHERE IsProcessed = 0 AND OrderDate > '2024-01-01'` runs, the optimizer can use `IX_Orders_Unprocessed`, scanning a much smaller index and returning results faster.

**Key tip:** Keep the filter predicate **sargable** (search‑argument‑able) and aligned with common query patterns to reap maximum benefits.  

---
