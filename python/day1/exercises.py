## I'm using combination of Freecodecamp, Youtube and cisco python programming course 
## These exercises are genarted by CHATGPT 

'''
Exercise 1: Hello Python
Print the following:
Hello, World!
I am learning Python.
'''
## There are 2 ways to print this 
#1st way :
print("Hello,World!")
print("I am learning Python")

#2nd way : Using "\n" to print in new line
print("Hello,World!\nI am learning Python")



'''
Exercise 2: Personal Information

Create variables for:

Your name
Your age
Your city

Print them using a single print() statement.

Example output:

Name: Rahul Age: 18 City: Mumbai
'''

name = "Asrith Behala"
age = 19
city = "Visakapatnam"

print("my name is "+ name + " i am " + str(age) + "years old and i am from " + city)


'''
Exercise 3: Data Types

Create variables:

name = "Alex"
age = 20
height = 5.8
is_student = True

Print the type of each variable using type().
'''

name = "Alex"
age = 20
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


'''
Exercise 4: Arithmetic Operators

Given:

a = 15
b = 4

Print:

Addition
Subtraction
Multiplication
Division
Modulus
Exponent
'''

a=15
b=4
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
exponent = a ** b
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulus)
print(exponent)


'''
Exercise 5: Comparison Operators

Given:

a = 10
b = 20

Print the result of:

a == b
a != b
a > b
a < b
a >= b
a <= b
'''

a = 10 
b = 20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# Exercise 6: Logical Operators

# Predict the output before running:

print(True and False)
print(True or False)
print(not True)
print(not False)


'''

Exercise 7: User Input

Ask the user for their name.

Example:

Enter your name: Broo
Hello Broo

'''

name = input("Enter your name:" )
print("Hello" + name)

'''
Exercise 8: Age Calculator

Ask the user for their age and print:

Next year you will be X years old.

Example:

Enter age: 18
Next year you will be 19 years old.

'''

age = input ("Enter your age : ")
print ("Next year you will be " + str(age+1) + " years old.")

'''
Exercise 9: Sum of Two Numbers

Take two numbers as input from the user.

Example:

Enter first number: 10
Enter second number: 20
Sum = 30
'''

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

Sum = number1 + number2
print("Sum = " + str(Sum))

'''
Exercise 10: Area of Rectangle

Take length and width as input from the user.

Area = length * width

'''

lenght = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))
Area = lenght * width
print("Area of the rectangle is : " + str(Area))

'''
Exercise 11: Square of a Number

Ask the user for a number and print its square.

Example:

Enter number: 5
Square = 25
'''

a = int(input("Enter a number : "))
square = a * a
print("Square of the number is : " + str(square))

'''

Exercise 12: Type Casting Practice

Predict the output:

a = "10"
b = 5

print(int(a) + b)

'''
# i predicted output would be : 15 
# as 10 is a string it gets converted to int and then added to 5 
'''
Exercise 13: Fix the Errors
1name = "Broo"
print(1name)

What's wrong?
'''
# the variable should not start with number so this will throw an error
