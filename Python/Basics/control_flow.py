# Variables & Control Flow in Depth

# 1. Variable Scoping
global_var = "I am global"

def scope_test():
    local_var = "I am local"
    print(global_var)
    print(local_var)

scope_test()

# 2. If-Elif-Else
age = 25
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 3. For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 4. While Loop with Break/Continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue # Skip even numbers
    if count > 7:
        break # Stop if count is greater than 7
    print(f"Odd count: {count}")
