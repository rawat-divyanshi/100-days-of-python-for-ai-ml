# ==========================================================
# Day 007 - Practice
# Topic: Loops (Part 2) & Logic Building
# ==========================================================

# ----------------------------------------------------------
# Example 1: Nested Loop
# ----------------------------------------------------------

# Outer loop controls rows
# Inner loop controls columns

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print()


# ----------------------------------------------------------
# Example 2: Number Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()


# ----------------------------------------------------------
# Example 3: Reverse Star Pattern
# ----------------------------------------------------------

for i in range(5, 0, -1):
    print("*" * i)

print()


# ----------------------------------------------------------
# Example 4: Right-Aligned Star Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

print()


# ----------------------------------------------------------
# Example 5: Loop with else
# ----------------------------------------------------------

for i in range(5):
    print(i)

else:
    print("Loop Completed Successfully")

print()


# ----------------------------------------------------------
# Example 6: Loop with break and else
# ----------------------------------------------------------

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("This will not execute.")

print()


# ----------------------------------------------------------
# Example 7: Prime Number Checker
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
# Example 8: Factorial
# ----------------------------------------------------------

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

print()


# ----------------------------------------------------------
# Example 9: Fibonacci Series
# ----------------------------------------------------------

terms = int(input("Enter number of terms: "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(terms):

    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print("\n")


# ----------------------------------------------------------
# Example 10: Multiplication Table
# ----------------------------------------------------------

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print()


# ----------------------------------------------------------
# Example 11: Sum of Digits
# ----------------------------------------------------------

number = int(input("Enter a number: "))

total = 0

while number > 0:

    digit = number % 10
    total += digit
    number //= 10

print("Sum of Digits =", total)

print()


# ----------------------------------------------------------
# Example 12: Reverse a Number
# ----------------------------------------------------------

number = int(input("Enter a number: "))

reverse = 0

while number > 0:

    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse =", reverse)

print()


# ----------------------------------------------------------
# Example 13: Count Digits
# ----------------------------------------------------------

number = int(input("Enter a number: "))

count = 0

while number > 0:
    count += 1
    number //= 10

print("Total Digits =", count)

print()


# ----------------------------------------------------------
# Example 14: Prime Numbers from 1 to 20
# ----------------------------------------------------------

print("Prime Numbers from 1 to 20:")

for num in range(2, 21):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print("\n")


# ----------------------------------------------------------
# Example 15: Number Pyramid
# ----------------------------------------------------------

for i in range(1, 6):

    for j in range(i):
        print(i, end=" ")

    print()

print()


# ----------------------------------------------------------
# Example 16: Multiplication Grid
# ----------------------------------------------------------

for i in range(1, 6):

    for j in range(1, 6):
        print(i * j, end="\t")

    print()

print()


# ----------------------------------------------------------
# Example 17: Triangle of Stars
# ----------------------------------------------------------

rows = 5

for i in range(1, rows + 1):
    print("* " * i)

print()


# ----------------------------------------------------------
# Example 18: Pattern using Characters
# ----------------------------------------------------------

for i in range(65, 70):

    for j in range(65, i + 1):
        print(chr(j), end=" ")

    print()

print()


# ----------------------------------------------------------
# Example 19: Find Largest Number
# ----------------------------------------------------------

largest = 0

for i in range(5):

    number = int(input(f"Enter number {i+1}: "))

    if number > largest:
        largest = number

print("Largest Number =", largest)

print()


# ----------------------------------------------------------
# Example 20: Countdown
# ----------------------------------------------------------

for i in range(10, 0, -1):
    print(i)

print("Happy Coding!")

print()

# ==========================================================
# End of Day 007 Practice
# ==========================================================