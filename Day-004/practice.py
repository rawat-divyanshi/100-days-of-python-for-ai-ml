# ==========================================================
# Day 004 - Practice
# Topic: Input, Type Conversion & Strings
# ==========================================================

# ----------------------------------------------------------
# Example 1: input() Function
# ----------------------------------------------------------

# input() is used to take input from the user.
name = input("Enter your name: ")

# Print the value entered by the user.
print("Hello,", name)

print()


# ----------------------------------------------------------
# Example 2: Type Conversion
# ----------------------------------------------------------

# input() always returns a string.
# Convert it into an integer using int().
age = int(input("Enter your age: "))

# Perform arithmetic on the integer value.
print("Your age after 5 years will be:", age + 5)

print()


# ----------------------------------------------------------
# Example 3: Creating Strings
# ----------------------------------------------------------

# Strings can be created using double quotes.
language = "Python"

# Strings can also be created using single quotes.
city = 'Delhi'

# Triple quotes are used for multi-line strings.
message = """
Welcome to Python Programming.
This is a multi-line string.
"""

print(language)
print(city)
print(message)

print()


# ----------------------------------------------------------
# Example 4: String Indexing
# ----------------------------------------------------------

word = "Python"

# Indexing starts from 0.
print("First Character :", word[0])

# Access the third character.
print("Third Character :", word[2])

# Negative indexing starts from the end.
print("Last Character :", word[-1])

# Access the second last character.
print("Second Last Character :", word[-2])

print()


# ----------------------------------------------------------
# Example 5: String Slicing
# ----------------------------------------------------------

text = "Programming"

# Get characters from index 0 to 3.
print("First Four Characters :", text[:4])

# Get characters from index 3 to the end.
print("From Index 3 :", text[3:])

# Get characters from index 2 to 7.
print("Index 2 to 7 :", text[2:8])

# Get every second character.
print("Every Second Character :", text[::2])

# Reverse the string.
print("Reverse String :", text[::-1])

print()


# ----------------------------------------------------------
# Example 6: String Immutability
# ----------------------------------------------------------

language = "Python"

# Strings cannot be modified character by character.
# The line below will produce an error if uncommented.

# language[0] = "J"

# Correct way: Create a new string.
language = "Jython"

print(language)

print()


# ----------------------------------------------------------
# Example 7: String Methods
# ----------------------------------------------------------

text = "   Python Programming   "

# Convert all letters to uppercase.
print(text.upper())

# Convert all letters to lowercase.
print(text.lower())

# Remove extra spaces from the beginning and end.
print(text.strip())

# Replace one word with another.
print(text.replace("Python", "Java"))

# Split the string into a list.
print(text.split())

# Join multiple strings together.
words = ["Python", "AI", "ML"]

print(" ".join(words))

# Format a string using format().
print("Hello {}!".format("Captain"))

print()


# ----------------------------------------------------------
# Example 8: f-Strings
# ----------------------------------------------------------

name = "Captain"
course = "Python for AI/ML"
day = 4

# f-strings are the recommended way to format strings.
print(f"My name is {name}.")
print(f"I am learning {course}.")
print(f"Today is Day {day} of my 100 Days of Code challenge.")

print()


# ----------------------------------------------------------
# Example 9: Combined Example
# ----------------------------------------------------------

# Take user input.
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_city = input("Enter your city: ")

print()

# Display the information using f-strings.
print(f"Hello {student_name}!")
print(f"You are {student_age} years old.")
print(f"You live in {student_city}.")
print(f"After 5 years, you will be {student_age + 5} years old.")

print()

print("===== End of Day 004 Practice =====")