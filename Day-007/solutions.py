# ==========================================================
# Day 007 - Solutions
# Topic: Loops (Part 2) & Logic Building
# ==========================================================

# ----------------------------------------------------------
# Q1
# Increasing Star Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    print("*" * i)

print()


# ----------------------------------------------------------
# Q2
# Number Triangle
# ----------------------------------------------------------

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()


# ----------------------------------------------------------
# Q3
# Fizz (Divisible by 3)
# ----------------------------------------------------------

for i in range(1, 21):

    if i % 3 == 0:
        print("Fizz")

    else:
        print(i)

print()


# ----------------------------------------------------------
# Q4
# Multiples of 5
# ----------------------------------------------------------

for i in range(5, 101, 5):
    print(i)

print()


# ----------------------------------------------------------
# Q5
# Sum of Even Numbers
# ----------------------------------------------------------

total = 0

for i in range(2, 51, 2):
    total += i

print("Sum =", total)

print()


# ==========================================================
# 🟡 Level 2
# ==========================================================

# ----------------------------------------------------------
# Q6
# Prime Number Checker
# ----------------------------------------------------------

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False

else:
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")

else:
    print("Not Prime Number")

print()


# ----------------------------------------------------------
# Q7
# Factorial
# ----------------------------------------------------------

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

print()


# ----------------------------------------------------------
# Q8
# Fibonacci Series
# ----------------------------------------------------------

first = 0
second = 1

print(first, second, end=" ")

for i in range(8):

    third = first + second
    print(third, end=" ")

    first = second
    second = third

print("\n")


# ----------------------------------------------------------
# Q9
# Count Digits
# ----------------------------------------------------------

number = int(input("Enter a number: "))

count = 0

while number > 0:
    number //= 10
    count += 1

print("Digits =", count)

print()


# ----------------------------------------------------------
# Q10
# Reverse a Number
# ----------------------------------------------------------

number = int(input("Enter a number: "))

reverse = 0

while number > 0:

    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse =", reverse)

print()


# ==========================================================
# 🔴 Level 3
# ==========================================================

# ----------------------------------------------------------
# Q11
# Reverse Star Pattern
# ----------------------------------------------------------

for i in range(5, 0, -1):
    print("*" * i)

print()


# ----------------------------------------------------------
# Q12
# Right-Aligned Star Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

print()


# ----------------------------------------------------------
# Q13
# Number Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    print(str(i) * (6 - i))

print()


# ----------------------------------------------------------
# Q14
# Prime Numbers from 1 to N
# ----------------------------------------------------------

limit = int(input("Enter a number: "))

for num in range(2, limit + 1):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print("\n")


# ----------------------------------------------------------
# Q15
# Sum of Digits
# ----------------------------------------------------------

number = int(input("Enter a number: "))

total = 0

while number > 0:

    digit = number % 10
    total += digit
    number //= 10

print("Sum of Digits =", total)

print()


# ==========================================================
# ⭐ Bonus Challenge
# Pattern Generator
# ==========================================================

print("1. Increasing Star Pattern")
print("2. Decreasing Star Pattern")
print("3. Number Triangle")
print("4. Multiplication Table")

choice = int(input("Enter your choice: "))

print()

if choice == 1:

    for i in range(1, 6):
        print("*" * i)

elif choice == 2:

    for i in range(5, 0, -1):
        print("*" * i)

elif choice == 3:

    for i in range(1, 6):

        for j in range(1, i + 1):
            print(j, end="")

        print()

elif choice == 4:

    number = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

else:
    print("Invalid Choice")

print()

# ==========================================================
# End of Solutions
# ==========================================================