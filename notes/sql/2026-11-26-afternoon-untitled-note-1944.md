# Untitled Note - 1944

**Category:** SQL  
**Date:** 2026-11-26 (afternoon)

---

# Table Partition Pruning

**What it is**  
Table partition pruning is the optimizer’s ability to skip whole partitions of a partitioned table when evaluating a query. Instead of scanning every partition, the engine evaluates the query’s predicates against the partitioning key and reads only the partitions that could contain matching rows.

**Why/where it’s useful**  
- **Large fact tables** (billions of rows) often use range or list partitioning on a date or region column.  
- Pruning dramatically reduces I/O, memory usage, and query latency because irrelevant partitions are never opened.  
- It works transparently for most SELECT, UPDATE, and DELETE statements, but the predicate must reference the partition key (or a deterministic function of it).  
- Helpful in data‑warehouse workloads, time‑series analytics, and multi‑tenant SaaS schemas.

**Example (PostgreSQL)**  

```sql
-- Create a range‑partitioned table on a timestamp column
CREATE TABLE events (
    id        BIGSERIAL PRIMARY KEY,
    event_ts  TIMESTAMP NOT NULL,
    payload   JSONB
) PARTITION BY RANGE (event_ts);

-- Define partitions per month
CREATE TABLE events_2023_01 PARTITION OF events
    FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');
CREATE TABLE events_2023_02 PARTITION OF events
    FOR VALUES FROM ('2023-02-01') TO ('2023-03-01');
-- ... more partitions ...

-- Query that benefits from pruning
EXPLAIN ANALYZE
SELECT * FROM events
WHERE event
