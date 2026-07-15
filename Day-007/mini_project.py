# ==========================================================
# Day 007 - Mini Project
# Project: Pattern Generator System
# ==========================================================

print("=" * 55)
print("          PATTERN GENERATOR SYSTEM")
print("=" * 55)

print("""
Choose a Pattern

1. Increasing Star Pattern
2. Decreasing Star Pattern
3. Number Triangle
4. Multiplication Table
5. Fibonacci Series
""")

choice = int(input("Enter your choice (1-5): "))

print()

# ----------------------------------------------------------
# Pattern 1
# ----------------------------------------------------------

if choice == 1:

    rows = int(input("Enter number of rows: "))

    print()

    for i in range(1, rows + 1):
        print("*" * i)

# ----------------------------------------------------------
# Pattern 2
# ----------------------------------------------------------

elif choice == 2:

    rows = int(input("Enter number of rows: "))

    print()

    for i in range(rows, 0, -1):
        print("*" * i)

# ----------------------------------------------------------
# Pattern 3
# ----------------------------------------------------------

elif choice == 3:

    rows = int(input("Enter number of rows: "))

    print()

    for i in range(1, rows + 1):

        for j in range(1, i + 1):
            print(j, end=" ")

        print()

# ----------------------------------------------------------
# Pattern 4
# ----------------------------------------------------------

elif choice == 4:

    number = int(input("Enter a number: "))

    print()

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# ----------------------------------------------------------
# Pattern 5
# ----------------------------------------------------------

elif choice == 5:

    terms = int(input("Enter number of terms: "))

    first = 0
    second = 1

    print()

    for i in range(terms):

        print(first, end=" ")

        next_number = first + second
        first = second
        second = next_number

    print()

# ----------------------------------------------------------
# Invalid Choice
# ----------------------------------------------------------

else:

    print("Invalid Choice!")

print()
print("=" * 55)
print("      Thank You for Using Pattern Generator")
print("=" * 55)