# Table Partitioning

**Category:** SQL  
**Date:** 2026-11-16 (afternoon)

---

# Table Partitioning

Table partitioning splits a large table into smaller, independent pieces called **partitions** while presenting a single logical view to queries. Each partition holds a subset of rows defined by a **partition key** (e.g., a date column). The database engine routes inserts, updates, and reads to the appropriate child table automatically.

**Why use it?**  
- **Performance:** Queries that filter on the partition key can prune irrelevant partitions, drastically reducing I/O.  
- **Maintenance:** Old partitions can be detached, archived, or dropped without locking the whole table.  
- **Scalability:** Each partition can be stored on different disks or even different nodes in some systems.  

**Typical use‑cases** include time‑series logs, billing records, or any dataset that grows continuously and is often queried by a range (e.g., “last month’s sales”).

### PostgreSQL Example (Range Partitioning)

```sql
-- Parent table (only metadata, no rows)
CREATE TABLE orders (
    order_id   BIGINT,
    order_date DATE NOT NULL,
    amount     NUMERIC
) PARTITION BY RANGE (order_date);

-- Create partitions for each quarter
CREATE TABLE orders_q1_2024 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE orders_q2_2024 PARTITION OF orders
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Insert – PostgreSQL routes automatically
INSERT INTO orders VALUES (101, '2024-02-15', 250.00);
```

When you query `SELECT * FROM orders WHERE order_date >= '2024-04-01'`, PostgreSQL scans only the Q2 partition, skipping Q1 entirely.

> **Tip:** Use `DEFAULT` partition to catch out‑of‑range rows and avoid insert errors.

---
