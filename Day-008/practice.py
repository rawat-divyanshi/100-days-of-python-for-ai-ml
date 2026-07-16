# ==========================================================
# Day 008 - Practice
# Topic: Functions (Part 1)
# ==========================================================

# ----------------------------------------------------------
# Example 1: Your First Function
# ----------------------------------------------------------

# Creating a simple function

def greet():
    print("Hello, Welcome to Python!")

# Calling the function
greet()

print()


# ----------------------------------------------------------
# Example 2: Calling a Function Multiple Times
# ----------------------------------------------------------

def welcome():
    print("Welcome Back!")

welcome()
welcome()
welcome()

print()


# ----------------------------------------------------------
# Example 3: Function with One Parameter
# ----------------------------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Amit")
greet_user("Python")

print()


# ----------------------------------------------------------
# Example 4: Function with Two Parameters
# ----------------------------------------------------------

def add(a, b):
    print("Sum =", a + b)

add(10, 20)
add(100, 50)

print()


# ----------------------------------------------------------
# Example 5: Function with Default Parameter
# ----------------------------------------------------------

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Amit")

print()


# ----------------------------------------------------------
# Example 6: Difference Between Parameter and Argument
# ----------------------------------------------------------

def student(name, course):
    print(name, "is learning", course)

student("Amit", "Python")

print()


# ----------------------------------------------------------
# Example 7: Function Returning a Value
# ----------------------------------------------------------

def square(number):
    return number * number

result = square(5)

print("Square =", result)

print()


# ----------------------------------------------------------
# Example 8: print() vs return
# ----------------------------------------------------------

def multiply(a, b):
    return a * b

answer = multiply(6, 7)

print(answer)

print()


# ----------------------------------------------------------
# Example 9: Even or Odd Checker
# ----------------------------------------------------------

def even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"

print(even_odd(15))
print(even_odd(20))

print()


# ----------------------------------------------------------
# Example 10: Maximum of Two Numbers
# ----------------------------------------------------------

def maximum(a, b):

    if a > b:
        return a

    return b

print("Maximum =", maximum(50, 80))

print()


# ----------------------------------------------------------
# Example 11: Area of Rectangle
# ----------------------------------------------------------

def rectangle_area(length, width):
    return length * width

print("Area =", rectangle_area(10, 5))

print()


# ----------------------------------------------------------
# Example 12: Celsius to Fahrenheit
# ----------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(30))

print()


# ----------------------------------------------------------
# Example 13: Factorial Function
# ----------------------------------------------------------

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

print(factorial(5))

print()


# ----------------------------------------------------------
# Example 14: Prime Number Function
# ----------------------------------------------------------

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True

print(is_prime(17))
print(is_prime(20))

print()


# ----------------------------------------------------------
# Example 15: Greeting Card Function
# ----------------------------------------------------------

def greeting(name, city):
    print("--------------------------")
    print("Name :", name)
    print("City :", city)
    print("--------------------------")

greeting("Amit", "Delhi")

print()


# ----------------------------------------------------------
# Example 16: Calculator Function
# ----------------------------------------------------------

def calculator(a, b):

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

calculator(20, 10)

print()


# ----------------------------------------------------------
# Example 17: Full Name Function
# ----------------------------------------------------------

def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Amit", "Rawat"))

print()


# ----------------------------------------------------------
# Example 18: Power Function
# ----------------------------------------------------------

def power(base, exponent):
    return base ** exponent

print(power(2, 5))

print()


# ----------------------------------------------------------
# Example 19: Age Checker
# ----------------------------------------------------------

def check_age(age):

    if age >= 18:
        return "Eligible to Vote"

    return "Not Eligible"

print(check_age(22))

print()


# ----------------------------------------------------------
# Example 20: Utility Function
# ----------------------------------------------------------

def display_line():
    print("=" * 40)

display_line()

print("Python Functions Practice")

display_line()

print()

# ==========================================================
# End of Day 008 Practice
# ==========================================================