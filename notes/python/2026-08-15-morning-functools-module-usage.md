# functools module usage

**Category:** Python  
**Date:** 2026-08-15 (morning)

---

# Python's `functools` Module
The `functools` module in Python provides functions for managing and extending other functions. It offers tools like `partial`, `update_wrapper`, and `total_ordering` to enhance and modify the behavior of existing functions. This module is particularly useful when working with higher-order functions, which are functions that take other functions as arguments or return functions as output.

In practice, the `functools` module is used in a variety of situations, such as creating partial functions with fixed arguments, preserving metadata of the original function when creating wrappers, and simplifying the implementation of classes that need to support total ordering. For instance, the `partial` function from this module can be used to create a new function with some arguments already filled in, which can be very handy when working with functions that require a lot of repetitive argument passing.

Here's a short example of using `partial`:
```python
import functools
import operator

add_five = functools.partial(operator.add, 5)
print(add_five(10))  # Outputs: 15
```
This example demonstrates how to create a new function `add_five` that adds 5 to any number passed to it, utilizing `functools.partial` and `operator.add`.
