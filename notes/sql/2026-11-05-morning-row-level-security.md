# Row-Level Security

**Category:** SQL  
**Date:** 2026-11-05 (morning)

---

# Row‑Level Security (RLS)

Row‑Level Security lets you restrict which rows a user can see or modify without altering the query itself. You define a security policy on a table that automatically adds a predicate (a `WHERE` clause) to every SELECT, UPDATE, DELETE, or INSERT executed by a role. The predicate can reference session variables such as `CURRENT_USER` or `SESSION_USER`, enabling fine‑grained access control.

**Why use it?**  
- **Multi‑tenant SaaS**: Isolate each tenant’s data while sharing a single schema.  
- **Regulatory compliance**: Enforce data‑privacy rules (e.g., GDPR) by limiting exposure to authorized personnel.  
- **Simpler application code**: No need to sprinkle tenant‑id filters throughout the codebase; the database enforces the rule centrally.

**Example (PostgreSQL)**  

```sql
-- 1. Create a table with a tenant identifier
CREATE TABLE orders (
    order_id   serial PRIMARY KEY,
    tenant_id  int NOT NULL,
    amount     numeric,
    created_at timestamp DEFAULT now()
);

-- 2. Enable row‑level security
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- 3. Define a policy that only shows rows belonging to the current tenant
CREATE POLICY tenant_isolation ON orders
    USING (tenant_id = current_setting('app.current_tenant')::int);

-- 4. Set the tenant context for a session
SET app.current_tenant = '42';

-- 5. All subsequent queries automatically respect the policy
SELECT * FROM orders;          -- returns only rows where tenant_id = 42
```

In this setup, any user that connects with the appropriate role will only see rows matching their `app.current_tenant` setting, and attempts to modify other rows will be blocked automatically.

---
