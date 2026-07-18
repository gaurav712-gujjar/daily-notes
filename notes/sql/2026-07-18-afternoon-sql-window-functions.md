# SQL Window Functions

**Category:** SQL  
**Date:** 2026-07-18 (afternoon)

---

# SQL Window Functions
SQL window functions are used to perform calculations across a set of table rows that are related to the current row, such as aggregating values or ranking rows. These functions are similar to aggregate functions, but they do not group rows into a single output row, instead, they return a value for each row.

Window functions are used in practice to solve complex query problems, such as calculating running totals, ranking rows, or accessing data from a previous row. They are particularly useful when working with large datasets and complex analytics.

For example, the following SQL query uses the `ROW_NUMBER()` window function to assign a unique number to each row in a table:
```sql
SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS row_num
FROM customers;
```
This query will return each row in the `customers` table with a unique `row_num` column, ordered by the `id` column.

Window functions are a powerful tool in SQL, allowing developers to write more efficient and effective queries.
