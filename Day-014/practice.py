"""
Day 14 - Practice
Topic: File Handling

Practice Programs:
- Opening and reading files
- Writing files
- Appending files
- Text file processing
- Word counting
- CSV files
- Context managers
- Practical file handling

Try to solve each program yourself before checking any reference solution.
"""


# ============================================================
# SECTION 1: READING FILES
# ============================================================

# Program 1
# Create "practice.txt" with some text.
# Then read and display the complete contents.


# Program 2
# Read "practice.txt" using readline()
# and display only the first line.


# Program 3
# Read "practice.txt" using readlines()
# and display all lines as a list.


# Program 4
# Read "practice.txt" and print each line separately
# using a for loop.


# Program 5
# Read a text file and count the total number of characters.


# ============================================================
# SECTION 2: WRITING FILES
# ============================================================

# Program 6
# Create "about_me.txt" and write:
#
# Name
# Age
# Course
# Goal
#
# into the file.


# Program 7
# Create "numbers.txt" and write numbers from 1 to 20,
# one number per line.


# Program 8
# Create "even_numbers.txt" and write only even numbers
# from 1 to 50.


# Program 9
# Create "subjects.txt" and write five subjects,
# one subject per line.


# Program 10
# Create "quotes.txt" and write three different quotes
# into the file.


# ============================================================
# SECTION 3: APPENDING FILES
# ============================================================

# Program 11
# Create "diary.txt" and write one diary entry.
# Then append another diary entry.


# Program 12
# Create "tasks.txt" and write three tasks.
# Append two additional tasks.


# Program 13
# Create "log.txt" and write:
#
# Program Started
#
# Then append:
#
# Program Running
# Program Completed
#
# Display the final file contents.


# Program 14
# Ask the user to enter a note.
# Append that note to "notes.txt".


# Program 15
# Create a file containing a list of students.
# Then append three more students.


# ============================================================
# SECTION 4: CONTEXT MANAGERS
# ============================================================

# Program 16
# Use a context manager to create "data.txt"
# and write some information into it.


# Program 17
# Use a context manager to read "data.txt"
# and display its contents.


# Program 18
# Use a context manager to count the number of lines
# in "data.txt".


# Program 19
# Use a context manager to count the number of words
# in "data.txt".


# Program 20
# Use a context manager to count the number of characters
# in "data.txt".


# ============================================================
# SECTION 5: TEXT FILE PROCESSING
# ============================================================

# Program 21
# Create "paragraph.txt" containing:
#
# Python is easy to learn.
# Python is useful for AI.
# Python is powerful.
#
# Count the total number of words.


# Program 22
# Read "paragraph.txt" and print every word separately.


# Program 23
# Read "paragraph.txt" and count how many times
# the word "Python" appears.


# Program 24
# Read a text file and count the number of lines.


# Program 25
# Read a text file and display the longest word.


# ============================================================
# SECTION 6: WORD OCCURRENCE
# ============================================================

# Program 26
# Create a text file containing:
#
# python is easy
# python is powerful
# python is useful
#
# Count how many times each word occurs.


# Program 27
# Take a sentence from the user.
# Save it into "input.txt".
# Read the file and count the words.


# Program 28
# Create a word counter that treats uppercase and lowercase
# words as the same.
#
# Example:
#
# Python python PYTHON
#
# Output:
#
# python: 3


# Program 29
# Create a word counter that ignores punctuation.
#
# Example:
#
# Python is easy!
# Python is powerful.
#
# "easy!" and "easy" should be treated as the same word.


# Program 30
# Read a text file and find the most frequently
# occurring word.


# ============================================================
# SECTION 7: CSV FILE PRACTICE
# ============================================================

# Program 31
# Create "students.csv" using the csv module.
#
# Columns:
# Name, Age, Marks
#
# Add at least five students.


# Program 32
# Read "students.csv" and display every row.


# Program 33
# Read "students.csv" and display only student names.


# Program 34
# Read "students.csv" and calculate:
#
# - Highest marks
# - Lowest marks
# - Average marks


# Program 35
# Create "products.csv" containing:
#
# Product, Price
#
# Add five products and display them.


# ============================================================
# SECTION 8: PRACTICAL FILE PROGRAMS
# ============================================================

# Program 36
# Create a program that asks the user for their name,
# age, and course.
#
# Save the information into "profile.txt".


# Program 37
# Create a program that asks the user for five tasks
# and saves them into "tasks.txt".


# Program 38
# Create a program that reads "tasks.txt" and displays:
#
# Total Tasks
# First Task
# Last Task


# Program 39
# Create a program that reads a text file and creates
# another file containing only the words with more than
# four characters.


# Program 40
# Create a program that reads a text file and creates
# a new file containing the text in uppercase.


# ============================================================
# SECTION 9: FILE-BASED DATA PROCESSING
# ============================================================

# Program 41
# Create a file containing numbers from 1 to 20.
# Read the file and calculate their sum.


# Program 42
# Create a file containing numbers.
# Read the numbers and find:
#
# - Maximum
# - Minimum
# - Average


# Program 43
# Read a text file and count:
#
# - Total words
# - Total characters
# - Total lines


# Program 44
# Read a text file and count the number of:
#
# - Vowels
# - Consonants


# Program 45
# Read a text file and create a new file containing
# only the unique words.


# ============================================================
# SECTION 10: MINI CHALLENGES
# ============================================================

# Program 46
# Create a simple Notes Manager.
#
# Menu:
#
# 1. Add Note
# 2. View Notes
# 3. Exit
#
# Store notes inside "notes.txt".


# Program 47
# Create a simple Student Record File.
#
# Store:
# - Name
# - Age
# - Marks
#
# Save each student record into "students.txt".


# Program 48
# Create a program that reads "students.txt"
# and displays all student records.


# Program 49
# Create a program that reads a text file and
# searches for a word entered by the user.
#
# Display:
#
# Word Found
# or
# Word Not Found


# Program 50
# Create a Text Analyzer.
#
# The program should:
#
# 1. Take text from the user.
# 2. Save it to "input.txt".
# 3. Read the file.
# 4. Count total words.
# 5. Count total characters.
# 6. Count total lines.
# 7. Count word occurrences.
# 8. Find the most frequent word.
# 9. Save word frequency to "word_count.txt".
#
# Example:
#
# Input:
# Python is easy and Python is powerful.
#
# Output:
#
# Total Words: 7
# Total Characters: ...
# Total Lines: 1
#
# Word Frequency:
# python: 2
# is: 2
# easy: 1
# and: 1
# powerful: 1
#
# ============================================================
# END OF DAY 14 PRACTICE
# ============================================================
