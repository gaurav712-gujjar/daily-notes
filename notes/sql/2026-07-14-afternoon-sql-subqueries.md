# SQL Subqueries

**Category:** SQL  
**Date:** 2026-07-14 (afternoon)

---

# SQL Subqueries
SQL subqueries are used to nest a query inside another query. This allows for more complex and dynamic querying capabilities, enabling the retrieval of data based on conditions that are themselves determined by a separate query. Subqueries can be used in various contexts, such as in the `WHERE`, `FROM`, or `SELECT` clauses of a main query.

In practice, subqueries are particularly useful when dealing with aggregate values or when the conditions for filtering data are dependent on other query results. For example, finding all employees who earn more than the average salary of their department can be achieved using a subquery to first calculate the average salary for each department.

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = 'Sales');
```

This example demonstrates a subquery in the `WHERE` clause, calculating the average salary for the 'Sales' department and then selecting employees with salaries higher than this average.
