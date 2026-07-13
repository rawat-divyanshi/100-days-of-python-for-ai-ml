# ==========================================================
# Day 006 - Solutions
# Topic: Loops (Part 1)
# ==========================================================

# ----------------------------------------------------------
# Q1
# Print numbers from 1 to 10.
# ----------------------------------------------------------

for i in range(1, 11):
    print(i)

print()


# ----------------------------------------------------------
# Q2
# Print your name 5 times.
# ----------------------------------------------------------

name = input("Enter your name: ")

for i in range(5):
    print(name)

print()


# ----------------------------------------------------------
# Q3
# Print numbers from 10 to 1.
# ----------------------------------------------------------

for i in range(10, 0, -1):
    print(i)

print()


# ----------------------------------------------------------
# Q4
# Print all even numbers from 1 to 20.
# ----------------------------------------------------------

for i in range(2, 21, 2):
    print(i)

print()


# ----------------------------------------------------------
# Q5
# Print all odd numbers from 1 to 20.
# ----------------------------------------------------------

for i in range(1, 21, 2):
    print(i)

print()


# ==========================================================
# 🟡 Level 2
# ==========================================================

# ----------------------------------------------------------
# Q6
# Multiplication Table
# ----------------------------------------------------------

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print()


# ----------------------------------------------------------
# Q7
# Print Squares
# ----------------------------------------------------------

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    print(i, "->", i * i)

print()


# ----------------------------------------------------------
# Q8
# Sum of 1 to 100
# ----------------------------------------------------------

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)

print()


# ----------------------------------------------------------
# Q9
# Numbers Divisible by 5
# ----------------------------------------------------------

limit = int(input("Enter the limit: "))

for i in range(1, limit + 1):

    if i % 5 == 0:
        print(i)

print()


# ----------------------------------------------------------
# Q10
# Star Pattern
# ----------------------------------------------------------

for i in range(1, 6):
    print("*" * i)

print()


# ==========================================================
# 🔴 Level 3
# ==========================================================

# ----------------------------------------------------------
# Q11
# Number Pattern
# ----------------------------------------------------------

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    print()

print()


# ----------------------------------------------------------
# Q12
# Count Even Numbers
# ----------------------------------------------------------

limit = int(input("Enter a number: "))

count = 0

for i in range(1, limit + 1):

    if i % 2 == 0:
        count += 1

print("Total Even Numbers =", count)

print()


# ----------------------------------------------------------
# Q13
# Factorial
# ----------------------------------------------------------

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)

print()


# ----------------------------------------------------------
# Q14
# Guess the Secret Number
# ----------------------------------------------------------

secret = 7

guess = 0

while guess != secret:

    guess = int(input("Guess the number: "))

print("Congratulations! You guessed correctly.")

print()


# ----------------------------------------------------------
# Q15
# Skip Number 10
# ----------------------------------------------------------

for i in range(1, 21):

    if i == 10:
        continue

    print(i)

print()


# ==========================================================
# ⭐ Bonus Challenge
# Number Series Generator
# ==========================================================

print("1. Even Numbers")
print("2. Odd Numbers")
print("3. Squares")
print("4. Multiplication Table")

choice = int(input("Enter your choice: "))
limit = int(input("Enter the limit: "))

print()

if choice == 1:

    for i in range(2, limit + 1, 2):
        print(i)

elif choice == 2:

    for i in range(1, limit + 1, 2):
        print(i)

elif choice == 3:

    for i in range(1, limit + 1):
        print(i * i)

elif choice == 4:

    for i in range(1, 11):
        print(f"{limit} x {i} = {limit * i}")

else:
    print("Invalid Choice")

print()

# ==========================================================
# End of Solutions
# ==========================================================