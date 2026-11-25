# System-Versioned Temporal Tables

**Category:** SQL  
**Date:** 2026-11-25 (afternoon)

---

# System‑Versioned Temporal Tables

A **system‑versioned temporal table** automatically tracks every row’s history by storing the period during which each version was valid. The database adds two hidden datetime columns (`SysStart`, `SysEnd`) and a history table that receives the old version whenever a row is updated or deleted. This feature lets you query data “as of” a point in time or retrieve the full change timeline without writing custom triggers or audit logs.

**Why use it?**  
- **Regulatory compliance** (e.g., GDPR, financial reporting) that requires immutable audit trails.  
- **Debugging / data recovery**: instantly view previous values or restore a row to an earlier state.  
- **Analytics**: analyze trends over time, such as price changes or employee role transitions, using simple temporal queries.

**Example (SQL Server)**  

```sql
-- Create the main table
CREATE TABLE Employees (
    EmpID   int PRIMARY KEY,
    Name    varchar(100),
    Salary  decimal(10,2),
    SysStart datetime2 GENERATED ALWAYS AS ROW START,
    SysEnd   datetime2 GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME (SysStart, SysEnd)
) WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.EmployeesHistory));

-- Update a row – the old version is automatically moved to EmployeesHistory
UPDATE Employees SET Salary = Salary * 1.05 WHERE EmpID = 7;

-- Query the table as it existed on a specific date
SELECT * FROM Employees 
FOR SYSTEM_TIME AS OF '2024-01-15 10:00:00' 
WHERE EmpID = 7;

-- Retrieve the full change history of a row
SELECT * FROM dbo.EmployeesHistory
WHERE EmpID = 7
ORDER BY SysStart DESC;
```

Temporal tables require minimal code overhead while delivering a reliable, query‑able audit log, making them a powerful tool for any application that needs built‑in data versioning.
