
"""
Day 14 - Exercise File
Topic: File Handling

Topics Covered:
- Opening files
- Reading files
- Writing files
- Appending files
- Working with .txt files
- Working with .csv files
- Context managers
- Word occurrence counting

Instructions:
Try to solve each exercise yourself before checking solutions.py.
"""


# ============================================================
# SECTION 1: OPENING AND READING FILES
# ============================================================

# Exercise 1
# Create a file named "example.txt" and write some text into it.
# Then open the file in read mode and print its contents.


# Exercise 2
# Read the complete contents of "example.txt" using read()
# and display them.


# Exercise 3
# Read only the first line of "example.txt" using readline()
# and print it.


# Exercise 4
# Read all lines of "example.txt" using readlines()
# and print the resulting list.


# Exercise 5
# Use a for loop to read and print each line of "example.txt"
# separately.


# ============================================================
# SECTION 2: WRITING TO FILES
# ============================================================

# Exercise 6
# Create a file named "message.txt" and write:
#
# Hello Python
# Welcome to File Handling
#
# into the file.


# Exercise 7
# Write the following student information into "student.txt":
#
# Name: Amit
# Age: 25
# Course: AI/ML
#
# Then read the file and display its contents.


# Exercise 8
# Create a file named "numbers.txt" and write numbers
# from 1 to 10 into the file, one number per line.


# Exercise 9
# Create a file named "subjects.txt" and write these subjects:
#
# Mathematics
# Python
# Machine Learning
# Statistics
#
# Each subject should appear on a separate line.


# ============================================================
# SECTION 3: APPENDING TO FILES
# ============================================================

# Exercise 10
# Create a file named "notes.txt" with the following content:
#
# Python is easy.
#
# Then append:
#
# Python is powerful.
#
# Finally, read and display the complete file.


# Exercise 11
# Create "log.txt" and write:
#
# Program Started
#
# Then append:
#
# Program Running
# Program Completed
#
# Display the final contents.


# Exercise 12
# Create a file named "tasks.txt" and write three tasks.
# Then append two more tasks to the same file.


# ============================================================
# SECTION 4: CONTEXT MANAGERS
# ============================================================

# Exercise 13
# Open "example.txt" using the with statement and print
# its contents.


# Exercise 14
# Write a program that creates "data.txt" using a
# context manager and writes some text into it.


# Exercise 15
# Read "data.txt" using a context manager and count
# the number of characters in the file.


# Exercise 16
# Read "data.txt" using a context manager and count
# the number of lines in the file.


# ============================================================
# SECTION 5: TEXT FILE PROCESSING
# ============================================================

# Exercise 17
# Create a file named "paragraph.txt" containing:
#
# Python is a programming language.
# Python is easy to learn.
# Python is useful for AI and ML.
#
# Read the file and count the total number of words.


# Exercise 18
# Read "paragraph.txt" and count the total number
# of characters.


# Exercise 19
# Read "paragraph.txt" and count how many times
# the word "Python" occurs.


# Exercise 20
# Read "paragraph.txt" and print every word separately.


# ============================================================
# SECTION 6: WORD OCCURRENCE COUNTER
# ============================================================

# Exercise 21
# Create a file named "text.txt" containing:
#
# python is easy
# python is powerful
# python is popular
#
# Read the file and count how many times each word occurs.
#
# Expected result:
#
# python: 3
# is: 3
# easy: 1
# powerful: 1
# popular: 1


# Exercise 22
# Create a word occurrence counter that reads any text
# entered by the user and saves it into "input.txt".
# Then read the file and count the words.


# Exercise 23
# Modify the word counter so that uppercase and lowercase
# words are treated as the same.
#
# Example:
#
# Python python PYTHON
#
# Expected:
#
# python: 3


# Exercise 24
# Create a word counter that ignores punctuation.
#
# Example:
#
# Python is easy!
# Python is powerful.
#
# Treat "easy!" and "easy" as the same word.


# Exercise 25
# Save the final word counts into a new file named
# "word_count.txt".
#
# Example output:
#
# python: 3
# is: 3
# easy: 1
# powerful: 1
# popular: 1


# ============================================================
# SECTION 7: CSV FILES
# ============================================================

# Exercise 26
# Create a CSV file named "students.csv" with the following
# columns:
#
# Name, Age, Marks
#
# Add at least three students.


# Exercise 27
# Read "students.csv" using the csv module and print
# every row.


# Exercise 28
# Read "students.csv" and print only the student names.


# Exercise 29
# Read "students.csv" and calculate the average marks.


# Exercise 30
# Create a CSV file named "products.csv" containing:
#
# Product, Price
#
# Add at least five products and display all products
# using the csv module.


# ============================================================
# BONUS EXERCISES
# ============================================================

# Bonus 1
# Create a program that:
#
# 1. Asks the user to enter a sentence.
# 2. Saves the sentence into "sentence.txt".
# 3. Reads the file.
# 4. Counts the words.
# 5. Displays the word count.


# Bonus 2
# Create a simple file-based student record system.
#
# Store:
# - Name
# - Age
# - Marks
#
# Save the information in "students.txt".


# Bonus 3
# Create a program that reads a text file and finds:
#
# - Total words
# - Total characters
# - Total lines
#
# Display all three results.


# Bonus 4
# Create a program that reads a text file and finds
# the most frequently occurring word.


# Bonus 5
# Create a program that reads a CSV file containing:
#
# Name, Marks
#
# and prints:
#
# - Highest marks
# - Lowest marks
# - Average marks


# ============================================================
# DAY 14 CHALLENGE
# ============================================================

# Create a program called "text_analyzer.py" that:
#
# 1. Takes text from the user.
# 2. Saves the text into "input.txt".
# 3. Reads the file.
# 4. Counts total words.
# 5. Counts total characters.
# 6. Counts word occurrences.
# 7. Displays the results.
# 8. Saves the word frequency into "word_count.txt".
#
# Example:
#
# Input:
# Python is easy and Python is powerful.
#
# Output:
#
# Total Words: 7
# Total Characters: 38
#
# Word Frequency:
# python: 2
# is: 2
# easy: 1
# and: 1
# powerful: 1
#
# ============================================================
# END OF DAY 14 EXERCISES
# ============================================================

