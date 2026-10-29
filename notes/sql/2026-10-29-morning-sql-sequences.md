# SQL Sequences

**Category:** SQL  
**Date:** 2026-10-29 (morning)

---

# SQL Sequences

A **sequence** is a database object that generates a series of numeric values according to a defined pattern (increment, start, min/max, cycle). Unlike identity columns, a sequence exists independently of any table, so multiple tables or rows can draw values from the same source.

**Why use it?**  
- **Surrogate keys** across several tables without coupling to a specific column.  
- **Batch inserts** where you need deterministic, gap‑free numbers (e.g., invoice numbers).  
- **Decoupling** generation logic from DML statements, allowing bulk loads or ETL pipelines to request identifiers without inserting rows immediately.

**Typical definition and usage (PostgreSQL / SQL Server syntax)**  

```sql
-- Create a sequence that starts at 1000 and increments by 5
CREATE SEQUENCE order_seq
    START WITH 1000
    INCREMENT BY 5
    NO MINVALUE
    NO MAXVALUE
    NO CYCLE;

-- Use NEXTVAL to fetch the next value
INSERT INTO orders (order_id, customer_id, total)
VALUES (NEXTVAL('order_seq'), 42, 199.99);

-- Retrieve current value without advancing
SELECT CURRVAL('order_seq');   -- 1000 after first insert
```

Sequences can also be referenced in `DEFAULT` clauses, enabling automatic key assignment:

```sql
CREATE TABLE invoices (
    invoice_id INT DEFAULT NEXTVAL('order_seq') PRIMARY KEY,
    amount NUMERIC(10,2)
);
```

Because a sequence is a standalone object, it can be granted privileges separately, providing fine‑grained control over who can generate identifiers.

---
