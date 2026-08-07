# Python Zip Function

**Category:** Python  
**Date:** 2026-08-07 (morning)

---

# Python Zip Function
The Python `zip` function is a built-in function that allows you to iterate over two or more lists in parallel. It takes the corresponding elements from each list and returns them as a tuple. This function is useful when you need to perform operations on multiple lists simultaneously.

In practice, the `zip` function is used in various scenarios, such as data processing, where you need to combine data from multiple sources. For example, you can use `zip` to iterate over two lists of names and ages, and create a dictionary where the names are the keys and the ages are the values.

Here's an example code snippet:
```python
names = ['John', 'Alice', 'Bob']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```
This code will output:
```
John is 25 years old
Alice is 30 years old
Bob is 35 years old
```
The `zip` function is a convenient and efficient way to iterate over multiple lists in parallel, making it a useful tool in many Python applications.
