# SQL Stored Procedures

**Category:** SQL  
**Date:** 2026-08-15 (afternoon)

---

# SQL Stored Procedures
SQL Stored Procedures are reusable blocks of code that perform a specific task, encapsulating complex logic and improving code organization. They are used to simplify database administration, reduce code duplication, and enhance security by limiting access to sensitive data.

In practice, stored procedures are used in various scenarios, such as data validation, data migration, and automated reporting. They can also be used to implement business logic, making it easier to maintain and update.

For example, a stored procedure can be created to insert a new employee into a database, performing necessary validation and formatting:
```sql
CREATE PROCEDURE sp_insert_employee
    @name nvarchar(50),
    @email nvarchar(100)
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM employees WHERE email = @email)
    BEGIN
        INSERT INTO employees (name, email)
        VALUES (@name, @email)
    END
    ELSE
    BEGIN
        RAISERROR ('Employee with this email already exists', 16, 1)
    END
END
```
This stored procedure checks if an employee with the given email already exists, and if not, inserts a new record into the `employees` table.
