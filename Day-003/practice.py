# ==========================================
# Day 003 - Practice Programs
# Topic: Python Operators
# ==========================================

# ------------------------------------------
# Arithmetic Operators
# ------------------------------------------

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)

print()

# ------------------------------------------
# Comparison Operators
# ------------------------------------------

x = 15
y = 10

print("Equal to:", x == y)
print("Not Equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or Equal to:", x >= y)
print("Less than or Equal to:", x <= y)

print()

# ------------------------------------------
# Logical Operators
# ------------------------------------------

age = 20

print("AND:", age > 18 and age < 30)
print("OR :", age > 18 or age > 50)
print("NOT:", not(age > 18))

print()

# ------------------------------------------
# Assignment Operators
# ------------------------------------------

number = 10
print("Initial Value:", number)

number += 5
print("After += 5 :", number)

number -= 3
print("After -= 3 :", number)

number *= 2
print("After *= 2 :", number)

number /= 4
print("After /= 4 :", number)

print()

# ------------------------------------------
# Bitwise Operators (Basic)
# ------------------------------------------

a = 5
b = 3

print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Left Shift (<<):", a << 1)
print("Right Shift (>>):", a >> 1)

print()

# ------------------------------------------
# Operator Precedence
# ------------------------------------------

print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)

print()

# ------------------------------------------
# Simple Calculator
# ------------------------------------------

num1 = 25
num2 = 5

print("Simple Calculator")
print("-----------------")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** 2)