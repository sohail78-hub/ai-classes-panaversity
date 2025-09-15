# Sohail Ahmed
# Batch 76 (Karachi)
# Roll No: PIAIC246962

# Assignment 1: Simple Calculator
# Date: 28-08-2025

#Q1: Variables & Data Types
print("\n---------------------------------------- \n")
print("Q1: Variables & Data Types")

name = "Sohail Ahmed"
age = 47
is_student = True

print("Name:", name, "Age:", age, "Is Student:", is_student)
print("Data Types - Name:", type(name), "Age:", type(age), "Is Student:", type(is_student))

#Q2: Basic Arithmetic Operations
print("\n---------------------------------------- \n")
print("Q2: Basic Arithmetic Operations")

x=20
y=6

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

#Q3: Assignment Operators
print("\n---------------------------------------- \n")
print("Q3: Assignment Operators")

num = 10

# 1. Add 5 to num using the += operator.
num += 5

# 2. Multiply num by 2 using the *= operator.
num *= 2

# 3. Subtract 4 from num using the -= operator.
num -= 4

print("Final value of num=", num)

#Q4: Comparison Operators
print("\n---------------------------------------- \n")
print("Q4: Comparison Operators")

a = 15
b = 12

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#Q5: Logical Operators
print("\n---------------------------------------- \n")
print("Q5: Logical Operators")

p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("not q:", not q)

# Q6: Real-Life Example
print("\n---------------------------------------- \n")
print("Q6: Real-Life Example")

notebook = 80
req_notbooks = 7

print("One Notebook =", notebook)
print("Amount of 7 notebooks =", req_notbooks*notebook)

pocket_amount = 600
print("Can buy Notebook from Pocket =", pocket_amount>=(req_notbooks*notebook))

# Bonu Question
print("\n---------------------------------------- \n")
print("Bonus Question")

a = int(input("Enter first Value: "))
b = int(input("Enter 2nd Value: "))

print("The result is: ",a+b)