# SQL Triggers and Automation

**Category:** SQL  
**Date:** 2026-09-23 (afternoon)

---

# SQL Triggers and Automation

A **trigger** is a special type of stored program that automatically executes in response to a defined data‑modification event (INSERT, UPDATE, DELETE) on a table or view. Triggers are stored in the database catalog and run on the server side, ensuring the logic is applied consistently regardless of the client application.

**Why use triggers?**  
- **Data integrity**: Enforce complex business rules that go beyond declarative constraints (e.g., preventing a salary increase that exceeds a percentage of the previous salary).  
- **Auditing**: Capture who changed what and when by writing rows to an audit log table.  
- **Derived data**: Keep summary tables, materialized views, or denormalized columns synchronized without extra application code.  
- **Security**: Restrict or modify operations based on session context (e.g., block DELETEs for non‑admin users).

**Basic syntax (PostgreSQL example)**

```sql
CREATE TABLE employees (
    emp_id   SERIAL PRIMARY KEY,
    name     TEXT,
    salary   NUMERIC,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Audit table
CREATE TABLE emp_audit (
    emp_id   INT,
    old_salary NUMERIC,
    new_salary NUMERIC,
    changed_at TIMESTAMP DEFAULT NOW()
);

-- Trigger function
CREATE OR REPLACE FUNCTION log_salary_change()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO emp_audit(emp_id, old_salary, new_salary)
    VALUES (OLD.emp_id, OLD.salary, NEW.salary);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach trigger to employees table
CREATE TRIGGER trg_salary_audit
AFTER UPDATE OF salary ON employees
FOR EACH ROW
WHEN (OLD.salary IS DISTINCT FROM NEW.salary)
EXECUTE FUNCTION log_salary_change();
```

In this example, every salary update automatically records the previous and new values in `emp_audit`, guaranteeing an immutable change history without any application‑level code.

---
