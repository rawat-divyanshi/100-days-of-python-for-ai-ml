# ==========================================================
# Day 004 - Assignment Solutions
# Topic: Input, Type Conversion & Strings
# ==========================================================

# ----------------------------------------------------------
# Part 1: input() Function
# ----------------------------------------------------------

# Q1
name = input("Enter your name: ")
print("Hello,", name)

print()

# Q2
language = input("Enter your favourite programming language: ")
print("My favourite programming language is", language)

print()

# ----------------------------------------------------------
# Part 2: Type Conversion
# ----------------------------------------------------------

# Q3
age = int(input("Enter your age: "))
print("Your age after 10 years will be:", age + 10)

print()

# Q4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)

print()

# Q5
price = float(input("Enter product price: "))

print("Data Type:", type(price))

print()

# ----------------------------------------------------------
# Part 3: Strings
# ----------------------------------------------------------

# Q6
country = "India"

print(country)

print()

# Q7
about = """
My name is Amit.
I am learning Python.
I want to become an AI/ML Engineer.
"""

print(about)

print()

# ----------------------------------------------------------
# Part 4: String Indexing
# ----------------------------------------------------------

word = "Programming"

# Q8
print(word[0])

# Q9
print(word[4])

# Q10
print(word[-1])

# Q11
print(word[-2])

print()

# ----------------------------------------------------------
# Part 5: String Slicing
# ----------------------------------------------------------

text = "Artificial Intelligence"

# Q12
print(text[:10])

# Q13
print(text[11:])

# Q14
print(text[::2])

# Q15
print(text[::-1])

print()

# ----------------------------------------------------------
# Part 6: String Methods
# ----------------------------------------------------------

sentence = "   Python is Amazing   "

# Q16
print(sentence.upper())

# Q17
print(sentence.lower())

# Q18
print(sentence.strip())

# Q19
print(sentence.replace("Amazing", "Powerful"))

# Q20
print(sentence.split())

print()

# ----------------------------------------------------------
# Part 7: join()
# ----------------------------------------------------------

words = ["Python", "AI", "ML"]

# Q21
print(" ".join(words))

# Q22
print("-".join(words))

print()

# ----------------------------------------------------------
# Part 8: format() and f-Strings
# ----------------------------------------------------------

# Q23
name = "Captain"

print("Hello {}".format(name))

print()

# Q24
name = "Captain"
age = 22
city = "Haridwar"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")

print()

# ----------------------------------------------------------
# Challenge Questions
# ----------------------------------------------------------

# Q25

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
language = input("Enter your favourite programming language: ")

print("\n===== Student Profile =====")
print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"City     : {city}")
print(f"Language : {language}")

print()

# Q26

text = "Python Programming"

print("First Character :", text[0])
print("Last Character :", text[-1])
print("First Six Characters :", text[:6])
print("Reverse :", text[::-1])

# ==========================================================
# End of Assignment Solutions
# ==========================================================