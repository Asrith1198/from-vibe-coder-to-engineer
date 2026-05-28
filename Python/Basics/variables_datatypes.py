# Day 1: Python Variables and Datatypes
# Based on UpGrad Course (https://learn.upgrad.com/course/1366)

# 1. Printing output
print("--- 1. Printing Output ---")
print("Hello, World!")  # We use print to output something to the screen.

# 2. Variables and Assignment
print("\n--- 2. Variables and Assignment ---")
a = 10
print("Initial value of a:", a)

# Variable Reassignment
a = 20
print("Reassigned value of a:", a)

# Multiple Assignments (Tuple Unpacking)
x, y = 100, 200
print("Multiple assignment x:", x, "y:", y)

# 3. Dynamic Typing & type() function
print("\n--- 3. Datatypes & type() function ---")

# String
message = "hi"
print("Value:", message, "| Type:", type(message))

# Integer
age = 23
print("Value:", age, "| Type:", type(age))

# Float (Decimals)
gpa = 8.5
print("Value:", gpa, "| Type:", type(gpa))

# Double (Python represents large precision decimals as standard float)
precise_val = 10.512345678987654321
print("Value:", precise_val, "| Type:", type(precise_val))

# Boolean
is_vibe_coder = True
print("Value:", is_vibe_coder, "| Type:", type(is_vibe_coder))
