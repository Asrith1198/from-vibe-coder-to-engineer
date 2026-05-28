# 🐍 Python Notes: Variables & Datatypes

> "Syntax is the grammar of code. Algorithms are the roadmap. Variables are the boxes we put our ideas in."

---

## 🎯 1. Fundamental Concepts

### What is Programming?
Programming is a **set of instructions** given to a computer to get a desired output.
* **Why can't we use human languages (like English, Telugu, or Hindi)?**
  Computers cannot understand the ambiguity and complexity of human languages directly. They require precise, strict languages designed for machine execution, such as Python or Java.
* **Why Python?**
  Python is highly expressive, reads almost like English, has simple syntax, and is the absolute industry standard for **AI and Machine Learning**, which is our ultimate goal!

### What is Python?
Python is an **Interpreted Programming Language**.
* **Interpreted vs. Compiled**:
  Unlike languages like C++ or Java which must be compiled (translated into machine code all at once) before running, Python reads and executes code line-by-line using an *Interpreter*. This makes development, testing, and debugging extremely fast and fluid!

### What is Syntax?
Syntax is the **grammar rules** of a programming language.
* Just like in English:
  * `"I am a student"` 🟢 Correct
  * `"I student am"` 🔴 Incorrect (Grammar/Syntax Error)
* In Python, if you do not follow the exact rules of punctuation and spacing, the Python interpreter will throw a `SyntaxError` and refuse to run.

### What is an Algorithm?
An algorithm is a **step-by-step procedure** to solve a specific problem. It is a finite, well-defined, and unambiguous sequence of instructions.

---

## 📦 2. Python Variables

Variables are labels or names used to reference data stored in computer memory.

### Rules for Naming Variables:
1. They generally start with a lowercase letter (e.g., `user_age`).
2. They **should not** start with a number (e.g., `1st_user` is invalid).
3. They **should not** contain any special characters (like `@`, `$`, `#`), except for the underscore `_`.
4. Python is case-sensitive (`age`, `Age`, and `AGE` are three different variables).

### Variable Assignment & Reassignment:
* We use the `=` operator to assign values to variables.
```python
# Simple Assignment
a = 10 
print(a)  # Output: 10

# Reassignment (Python dynamically updates the reference)
a = 20
print(a)  # Output: 20

# Multiple Assignment (Tuple unpacking)
x, y = 100, 200
print(x, y)  # Output: 100 200
```

---

## 📊 3. Python Datatypes & Dynamic Typing

In languages like C or Java, you must declare what datatype a variable holds beforehand (`int a = 10;`).
Python uses **Dynamic Typing**: it automatically determines the datatype of a variable based on the value assigned to it.

We can use the `type()` built-in function to inspect the datatype of any variable.

| Datatype | Description | Python Class | Example |
| :--- | :--- | :--- | :--- |
| **String** | Anything enclosed in double `""` or single `''` quotes. Stores characters, spaces, and numbers as text. | `<class 'str'>` | `name = "Asrith"` |
| **Integer** | Whole numbers (positive, negative, or zero). | `<class 'int'>` | `age = 23` |
| **Float** | Any decimal number. | `<class 'float'>` | `gpa = 8.5` |
| **Double** | Double-precision decimals. In Python, standard floats are double-precision under the hood. | `<class 'float'>` | `precise = 10.51234567898` |
| **Boolean** | Logical truth values. Can only be `True` or `False`. | `<class 'bool'>` | `is_active = True` |

```python
# Code example to print types:
a = "hi"
print(type(a))  # Output: <class 'str'>

b = 10.5
print(type(b))  # Output: <class 'float'>

c = True
print(type(c))  # Output: <class 'bool'>
```
