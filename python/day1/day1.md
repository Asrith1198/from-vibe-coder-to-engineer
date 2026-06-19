# Day 1 - Introduction to Python

## What I Learned Today

Today I started learning **Python Programming**.

### What is Programming?

* Programming is the process of giving instructions to a computer.
* Computers understand only binary language (0s and 1s).
* Python code is converted into machine language using an **Interpreter**.

### Why Python?

I learned that Python is:

* Easy to read and write
* Similar to English language
* Free and open-source
* Used in AI, Machine Learning, Web Development, Data Science, and Automation

---

## Python Setup

I learned how to install Python and verify the installation using:

```bash
python3 --version
```

Python programs are saved with the `.py` extension.

Example:

```python
hello.py
```

---

## Output in Python

To display something on the screen, Python uses the `print()` function.

Example:

```python
print("Hello World")
```

I also learned that multiple values can be printed together:

```python
print("Hello", "Python")
```

---

## Variables

Variables are used to store data in memory.

Example:

```python
name = "John"
age = 20
```

### Rules for Variable Names

* Can contain letters, numbers, and underscores
* Cannot start with a number
* Are case-sensitive

Example:

```python
name = "Ram"
Name = "Shyam"
```

These are considered different variables.

---

## Data Types

### String (`str`)

Stores text.

```python
name = "Python"
```

### Integer (`int`)

Stores whole numbers.

```python
age = 20
```

### Float (`float`)

Stores decimal values.

```python
price = 99.99
```

### Boolean (`bool`)

Stores `True` or `False`.

```python
is_student = True
```

### None

Represents no value.

```python
x = None
```

### Checking Data Types

```python
print(type(age))
```

---

## Comments

Comments are ignored by Python during execution.

### Single-Line Comment

```python
# This is a comment
```

### Multi-Line Comment

```python
'''
This is a
multi-line comment
'''
```

---

## Operators

### Arithmetic Operators

| Operator | Purpose        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| %        | Remainder      |
| **       | Power          |

### Comparison Operators

| Operator | Purpose               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

These operators return `True` or `False`.

### Assignment Operators

```python
=
+=
-=
*=
/=
```

### Logical Operators

```python
and
or
not
```

---

## Type Conversion and Type Casting

Python can automatically convert compatible types.

Example:

```python
10 + 5.5
```

Result:

```python
15.5
```

### Type Casting

Used to manually convert data types.

```python
int()
float()
str()
```

Example:

```python
num = int("10")
```

---

## User Input

Python uses the `input()` function to get data from the user.

Example:

```python
name = input("Enter your name: ")
```

### Important Point

`input()` always returns a string.

If I need a number, I must convert it:

```python
age = int(input("Enter age: "))
```

or

```python
salary = float(input("Enter salary: "))
```

---

## Key Takeaways

* Programming means giving instructions to a computer.
* Python uses an Interpreter.
* Python files use the `.py` extension.
* `print()` is used for output.
* `input()` is used for user input.
* Main data types are `str`, `int`, `float`, `bool`, and `None`.
* Comments improve code readability.
* Operators perform calculations and comparisons.
* `input()` always returns a string.
* Type casting is done using `int()`, `float()`, and `str()`.

## Today's Progress

* Installed Python
* Learned basic syntax
* Learned variables and data types
* Learned comments and operators
* Learned user input and type casting

**End of Day 1 Notes**
