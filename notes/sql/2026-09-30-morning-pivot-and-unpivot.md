# Pivot and Unpivot

**Category:** SQL  
**Date:** 2026-09-30 (morning)

---

# Pivot and Unpivot

**Concept**  
`PIVOT` and `UNPIVOT` are T‑SQL operators that reshape result sets by rotating rows into columns (pivot) or columns into rows (unpivot). They are handy when you need a cross‑tabular view of data without writing complex `CASE` expressions.

**When to use**  
- **Reporting dashboards** where each metric should appear as its own column (e.g., sales per quarter).  
- **Data preparation** for feeding into BI tools that expect a wide format.  
- Converting a normalized key‑value table into a denormalized matrix for quick analysis.

**Example**  

```sql
-- Sample data: sales by product and month
CREATE TABLE Sales (Product VARCHAR(20), SalesMonth CHAR(3), Qty INT);
INSERT INTO Sales VALUES
('Bike', 'Jan', 10), ('Bike', 'Feb', 12),
('Bike', 'Mar', 14), ('Glove', 'Jan', 5),
('Glove', 'Feb', 7), ('Glove', 'Mar', 6);

-- Pivot: months become columns
SELECT Product, [Jan], [Feb], [Mar]
FROM (
    SELECT Product, SalesMonth, Qty FROM Sales
) s
PIVOT (
    SUM(Qty) FOR SalesMonth IN ([Jan], [Feb], [Mar])
) p;
```

Result:

| Product | Jan | Feb | Mar |
|---------|-----|-----|-----|
| Bike    | 10  | 12  | 14  |
| Glove   | 5   | 7   | 6   |

The opposite transformation uses `UNPIVOT`:

```sql
SELECT Product, SalesMonth, Qty
FROM (
    SELECT Product, [Jan], [Feb], [Mar] FROM PivotResult
) p
UNPIVOT (
    Qty FOR SalesMonth IN ([Jan], [Feb], [Mar])
) u;
```

These operators simplify data reshaping, improve query readability, and often perform better than manual `CASE`‑based pivots.
