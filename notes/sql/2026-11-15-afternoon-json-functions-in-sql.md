# JSON Functions in SQL

**Category:** SQL  
**Date:** 2026-11-15 (afternoon)

---

# JSON Functions in SQL

JSON (JavaScript Object Notation) is a lightweight data‑interchange format that many modern applications use for APIs and configuration. Relational databases such as PostgreSQL, MySQL, SQL Server, and Oracle now provide native JSON data types and a suite of functions to store, query, and manipulate JSON directly in SQL tables.  

**Why it matters**  
- **Schema flexibility** – Store semi‑structured data without redesigning the schema.  
- **Hybrid workloads** – Combine relational joins with document‑style queries in a single engine.  
- **Performance** – Index JSON fields (e.g., GIN in PostgreSQL, JSON indexes in MySQL) for fast lookups, avoiding costly application‑side parsing.  

**Typical use‑cases**  
- Logging events where each event may have different attributes.  
- Caching API responses in a table for quick retrieval.  
- Storing configuration blobs that evolve over time.

**Example (PostgreSQL)**  

```sql
-- Table with a native jsonb column
CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INT,
    payload     JSONB          -- stores the order details
);

-- Insert a JSON document
INSERT INTO orders (customer_id, payload) VALUES
(42, '{"items":[{"sku":"A123","qty":2},{"sku":"B456","qty":1}],
       "total": 59.99,
       "status":"pending"}');

-- Query orders containing a specific SKU
SELECT id, payload->>'status' AS status
FROM orders
WHERE payload @> '{"items":[{"sku":"A123"}]}';
```

The `@>` operator checks containment, while `->>` extracts a scalar value. By indexing `payload` with a GIN index, the query runs efficiently even on millions of rows.

---
