# SQL Isolation Levels

**Category:** SQL  
**Date:** 2026-11-26 (morning)

---

# SQL Isolation Levels

Isolation levels define how concurrent transactions interact with each other, controlling phenomena such as dirty reads, non‑repeatable reads, and phantom rows. The SQL standard (and most RDBMSs) support four classic levels:

| Level | Guarantees | Typical Use |
|-------|------------|-------------|
| **READ UNCOMMITTED** | Allows dirty reads; no locks are taken. | Bulk analytics where stale data is acceptable. |
| **READ COMMITTED** | Prevents dirty reads; data can change between reads. | Default in PostgreSQL, Oracle; balances consistency and concurrency. |
| **REPEATABLE READ** | Prevents dirty and non‑repeatable reads; rows read stay stable. | Reporting queries that must see a stable snapshot. |
| **SERIALIZABLE** | Full isolation; transactions appear to run sequentially. | Critical financial updates where absolute correctness is required. |

Choosing the right level is a trade‑off between consistency and performance. Higher isolation incurs more locking or versioning overhead, potentially reducing throughput.

**Example (PostgreSQL)**  

```sql
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SELECT balance FROM accounts WHERE id = 42;   -- first read
-- other sessions may modify the row here, but this transaction still sees the original value
SELECT balance FROM accounts WHERE id = 42;   -- second read returns the same value

COMMIT;
```

In this block, the transaction sees a consistent snapshot even if other sessions update the `accounts` row concurrently. Switching to `SERIALIZABLE` would additionally block inserts that could create phantom rows affecting range queries.

Understanding isolation levels helps you tune concurrency control to match the correctness needs of your application.
