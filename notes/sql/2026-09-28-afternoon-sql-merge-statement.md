# SQL MERGE Statement

**Category:** SQL  
**Date:** 2026-09-28 (afternoon)

---

# SQL MERGE Statement

The `MERGE` statement, sometimes called “upsert”, lets you combine `INSERT`, `UPDATE`, and `DELETE` logic into a single, set‑based operation. It matches rows from a source query to a target table using a join condition; based on whether a match is found, you can specify actions for `WHEN MATCHED` (update or delete) and `WHEN NOT MATCHED` (insert).  

**Why use it?**  
- Eliminates the need for separate `SELECT` → conditional `INSERT`/`UPDATE` code, reducing round‑trips and race conditions.  
- Guarantees atomicity: the whole merge runs as one transaction, preventing partial updates.  
- Ideal for data‑warehouse loading, synchronizing master‑detail tables, or applying change‑feeds.

**Example**

```sql
MERGE INTO inventory AS tgt
USING (SELECT sku, qty FROM incoming_stock) AS src
ON tgt.sku = src.sku
WHEN MATCHED THEN
    UPDATE SET tgt.qty = tgt.qty + src.qty
WHEN NOT MATCHED THEN
    INSERT (sku, qty) VALUES (src.sku, src.qty);
```

In this snippet, existing SKUs have their quantity increased, while new SKUs are inserted. If you also need to delete rows that are no longer present in the source, add a `WHEN NOT MATCHED BY SOURCE THEN DELETE` clause.
