# Day 13: String Manipulation - Regular Expressions
# EXERCISES (Topics 1-3)

import re

# ==========================================
# TOPIC 1 & 2: Basic Pattern Exercises
# ==========================================

# Exercise 1: Find all digits in a string
print("=== Exercise 1: Find all digits ===")
text1 = "My ID is 12345 and PIN is 6789"
# TODO: Use re.findall() to find all digits
# Expected: ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Exercise 2: Find all numbers grouped together
print("\n=== Exercise 2: Find grouped numbers ===")
text2 = "Price: 100, Discount: 25, Final: 75"
# TODO: Use re.findall() to find all complete numbers
# Expected: ['100', '25', '75']


# Exercise 3: Find all lowercase words
print("\n=== Exercise 3: Find lowercase words ===")
text3 = "Hello World Python Programming"
# TODO: Use re.findall() to find only lowercase letters
# Expected: ['ello', 'orld', 'ython', 'rogramming']


# Exercise 4: Find all words (any case)
print("\n=== Exercise 4: Find all words ===")
text4 = "Hello123 World456 Python789"
# TODO: Use re.findall() to find all words (letters only)
# Expected: ['Hello', 'World', 'Python']


# Exercise 5: Find all uppercase letters
print("\n=== Exercise 5: Find uppercase letters ===")
text5 = "PythonAIML"
# TODO: Use re.findall() to find only uppercase letters
# Expected: ['P', 'A', 'I', 'M', 'L']


# Exercise 6: Find sequences of digits (1+ digits)
print("\n=== Exercise 6: Find digit sequences ===")
text6 = "User123 Admin456 Guest789"
# TODO: Use re.findall() to find all number sequences
# Expected: ['123', '456', '789']


# Exercise 7: Find words with letters only (no numbers)
print("\n=== Exercise 7: Find letter-only words ===")
text7 = "hello123 world python456"
# TODO: Use re.findall() to