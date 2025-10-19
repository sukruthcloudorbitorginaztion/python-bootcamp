# Assignment: Floating Point Number Class

## Objective

The objective of this assignment is to **implement a custom floating-point number class** that performs arithmetic and comparison operations with **maximum precision and accuracy** without relying on Python’s built-in floating-point arithmetic.

This assignment aims to strengthen your understanding of:

* **Object-Oriented Programming (OOP)** in Python
* **Operator overloading** (`__add__`, `__sub__`, `__eq__`, etc.)
* **Precision handling** of floating-point numbers
* **String parsing** and **integer-based arithmetic** for accurate decimal operations

---

## Required Skills

Before attempting this problem, you should be comfortable with:

* Python class design and constructors (`__init__`)
* Instance attributes and methods
* Magic methods / Dunder methods (`__add__`, `__sub__`, `__str__`, `__eq__`, `__ne__`)
* String manipulation and numeric conversions
* Writing and executing unit tests (e.g., using `pytest`)

---

## Problem Statement

In standard floating-point arithmetic (using Python’s built-in `float` type), precision errors often occur due to binary representation limitations.

Your task is to create a class **`FloatingPointNumber`** that simulates floating-point arithmetic using **integer arithmetic under the hood** — allowing precise representation and accurate operations even for long decimals.

You must implement:

1. **Addition (`+`)**
2. **Subtraction (`-`)**
3. **Equality (`==`) and inequality (`!=`) comparison**
4. **String conversion (`str()`)**

The class should:

* Accept floating-point numbers as **strings** during initialization (e.g., `"123.456789"`).
* Support both **positive** and **negative** numbers.
* Perform operations without precision loss.
* Handle numbers **with or without fractional parts** (e.g., `"42"`, `"42.0"`).

---

## Sample Input and Output

### Example 1

```python
obj1 = FloatingPointNumber("-0.5")
obj2 = FloatingPointNumber("-10.92")

print(obj1 + obj2)  # Output: -11.42
print(obj1 - obj2)  # Output: 10.42
print(obj1 + 0.5)   # Output: 0
print(obj1 == obj2) # Output: False
```

### Example 2

```python
a = FloatingPointNumber("123.456")
b = FloatingPointNumber("76.544")

print(a + b)  # Output: 200.0
print(a - b)  # Output: 46.912
```

---

## Hints & Tips

* Always **store integer and fractional parts separately** for each number.
* Handle **signs carefully** during addition and subtraction — the logic should work for negative inputs too.
* When aligning decimals during arithmetic:

  * Determine the maximum fractional length of the operands.
  * Multiply both fractions accordingly to achieve equal precision before performing integer arithmetic.
* After performing operations, **rebuild the result string** using integer and fractional parts.
* When comparing two numbers (`==` or `!=`), comparing their string representations is often sufficient.
* Use **unit testing** to validate your class.
  Example with `pytest`:

  ```bash
  pytest -v tests/test_floating_point_number.py
  ```

---

## Deliverables

1. **Source Code**
   File: `python_bootcamp_cloudorbit\chapter3\floating_point_number.py`
   Containing the implementation of the `FloatingPointNumber` class with:

   * `__init__`
   * `__add__`
   * `__sub__`
   * `__eq__`
   * `__ne__`
   * `__str__`



