
"""
Day 14 - Solutions
Topic: File Handling

Solutions for all exercises, bonus exercises,
and the Day 14 Challenge.

Topics:
- Opening files
- Reading files
- Writing files
- Appending files
- Working with .txt files
- Working with .csv files
- Context managers
- Word occurrence counting
"""


import csv
import string


# ============================================================
# SECTION 1: OPENING AND READING FILES
# ============================================================

# Exercise 1
# Create a file named "example.txt" and write some text into it.
# Then open the file in read mode and print its contents.

with open("example.txt", "w") as file:
    file.write("Hello Python!\nWelcome to File Handling.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Exercise 2
# Read the complete contents of "example.txt" using read()
# and display them.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Exercise 3
# Read only the first line of "example.txt" using readline()
# and print it.

with open("example.txt", "r") as file:
    first_line = file.readline()
    print(first_line)


# Exercise 4
# Read all lines of "example.txt" using readlines()
# and print the resulting list.

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# Exercise 5
# Use a for loop to read and print each line separately.

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================================
# SECTION 2: WRITING TO FILES
# ============================================================

# Exercise 6
# Create "message.txt" and write the given text.

with open("message.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling\n")


# Exercise 7
# Write student information and then read it.

with open("student.txt", "w") as file:
    file.write("Name: Amit\n")
    file.write("Age: 25\n")
    file.write("Course: AI/ML\n")

with open("student.txt", "r") as file:
    print(file.read())


# Exercise 8
# Write numbers from 1 to 10, one number per line.

with open("numbers.txt", "w") as file:
    for number in range(1, 11):
        file.write(f"{number}\n")


# Exercise 9
# Write subjects into "subjects.txt".

subjects = [
    "Mathematics",
    "Python",
    "Machine Learning",
    "Statistics"
]

with open("subjects.txt", "w") as file:
    for subject in subjects:
        file.write(f"{subject}\n")


# ============================================================
# SECTION 3: APPENDING TO FILES
# ============================================================

# Exercise 10
# Create the file and append new content.

with open("notes.txt", "w") as file:
    file.write("Python is easy.\n")

with open("notes.txt", "a") as file:
    file.write("Python is powerful.\n")

with open("notes.txt", "r") as file:
    print(file.read())


# Exercise 11
# Create log.txt and append two more messages.

with open("log.txt", "w") as file:
    file.write("Program Started\n")

with open("log.txt", "a") as file:
    file.write("Program Running\n")
    file.write("Program Completed\n")

with open("log.txt", "r") as file:
    print(file.read())


# Exercise 12
# Create three tasks and append two more.

with open("tasks.txt", "w") as file:
    file.write("Study Python\n")
    file.write("Practice File Handling\n")
    file.write("Complete Exercises\n")

with open("tasks.txt", "a") as file:
    file.write("Review Notes\n")
    file.write("Build Mini Project\n")

with open("tasks.txt", "r") as file:
    print(file.read())


# ============================================================
# SECTION 4: CONTEXT MANAGERS
# ============================================================

# Exercise 13
# Open example.txt using the with statement.

with open("example.txt", "r") as file:
    print(file.read())


# Exercise 14
# Create data.txt using a context manager.

with open("data.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Learning Python for AI/ML")


# Exercise 15
# Count characters in data.txt.

with open("data.txt", "r") as file:
    data = file.read()

character_count = len(data)

print("Character Count:", character_count)


# Exercise 16
# Count lines in data.txt.

with open("data.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)

print("Line Count:", line_count)


# ============================================================
# SECTION 5: TEXT FILE PROCESSING
# ============================================================

# Exercise 17
# Create paragraph.txt and count total words.

paragraph = """Python is a programming language.
Python is easy to learn.
Python is useful for AI and ML."""

with open("paragraph.txt", "w") as file:
    file.write(paragraph)

with open("paragraph.txt", "r") as file:
    text = file.read()

words = text.split()

print("Total Words:", len(words))


# Exercise 18
# Count total characters in paragraph.txt.

with open("paragraph.txt", "r") as file:
    text = file.read()

print("Total Characters:", len(text))


# Exercise 19
# Count how many times "Python" occurs.

with open("paragraph.txt", "r") as file:
    text = file.read()

python_count = text.count("Python")

print("Python occurs:", python_count, "times")


# Exercise 20
# Print every word separately.

with open("paragraph.txt", "r") as file:
    text = file.read()

words = text.split()

for word in words:
    print(word)


# ============================================================
# SECTION 6: WORD OCCURRENCE COUNTER
# ============================================================

# Exercise 21
# Count word occurrences in text.txt.

text = """python is easy
python is powerful
python is popular"""

with open("text.txt", "w") as file:
    file.write(text)

with open("text.txt", "r") as file:
    text = file.read()

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")


# Exercise 22
# Take text from the user, save it, read it, and count words.

user_text = input("Enter some text: ")

with open("input.txt", "w") as file:
    file.write(user_text)

with open("input.txt", "r") as file:
    text = file.read()

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# Exercise 23
# Treat uppercase and lowercase words as the same.

text = "Python python PYTHON"

words = text.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


# Exercise 24
# Ignore punctuation while counting words.

text = """Python is easy!
Python is powerful."""

words = text.lower().split()

cleaned_words = []

for word in words:
    word = word.strip(string.punctuation)
    cleaned_words.append(word)

word_count = {}

for word in cleaned_words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")


# Exercise 25
# Save word counts into word_count.txt.

text = """python is easy
python is powerful
python is popular"""

words = text.lower().split()

word_count = {}

for word in words:
    word = word.strip(string.punctuation)
    word_count[word] = word_count.get(word, 0) + 1

with open("word_count.txt", "w") as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")

print("Word counts saved to word_count.txt")


# ============================================================
# SECTION 7: CSV FILES
# ============================================================

# Exercise 26
# Create students.csv with at least three students.

students = [
    ["Name", "Age", "Marks"],
    ["Amit", 25, 85],
    ["Rahul", 24, 90],
    ["Priya", 23, 88]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)


# Exercise 27
# Read students.csv and print every row.

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 28
# Print only the student names.

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row[0])


# Exercise 29
# Calculate average marks.

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    marks = []

    for row in reader:
        marks.append(float(row[2]))

average_marks = sum(marks) / len(marks)

print("Average Marks:", average_marks)


# Exercise 30
# Create products.csv and display all products.

products = [
    ["Product", "Price"],
    ["Laptop", 60000],
    ["Mouse", 800],
    ["Keyboard", 1500],
    ["Monitor", 12000],
    ["Headphones", 2500]
]

with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(products)

with open("products.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ============================================================
# BONUS EXERCISES
# ============================================================

# Bonus 1
# Take a sentence, save it, read it, and count words.

sentence = input("Enter a sentence: ")

with open("sentence.txt", "w") as file:
    file.write(sentence)

with open("sentence.txt", "r") as file:
    text = file.read()

word_count = len(text.split())

print("Word Count:", word_count)


# Bonus 2
# Simple file-based student record system.

name = input("Enter student name: ")
age = input("Enter student age: ")
marks = input("Enter student marks: ")

with open("students.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Marks: {marks}\n")

print("Student record saved.")


# Bonus 3
# Find total words, characters, and lines.

with open("paragraph.txt", "r") as file:
    text = file.read()

total_words = len(text.split())
total_characters = len(text)
total_lines = len(text.splitlines())

print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Total Lines:", total_lines)


# Bonus 4
# Find the most frequently occurring word.

with open("paragraph.txt", "r") as file:
    text = file.read().lower()

words = text.split()

word_count = {}

for word in words:
    word = word.strip(string.punctuation)
    word_count[word] = word_count.get(word, 0) + 1

most_frequent_word = max(word_count, key=word_count.get)

print("Most Frequent Word:", most_frequent_word)
print("Frequency:", word_count[most_frequent_word])


# Bonus 5
# Read a CSV file and calculate highest, lowest,
# and average marks.

marks_data = [
    ["Name", "Marks"],
    ["Amit", 85],
    ["Rahul", 90],
    ["Priya", 88],
    ["Neha", 92]
]

with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(marks_data)

with open("marks.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    marks = [float(row[1]) for row in reader]

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))


# ============================================================
# DAY 14 CHALLENGE
# ============================================================

# Text Analyzer
#
# 1. Take text from the user.
# 2. Save it into input.txt.
# 3. Read the file.
# 4. Count total words.
# 5. Count total characters.
# 6. Count word occurrences.
# 7. Display the results.
# 8. Save word frequency into word_count.txt.


user_text = input("\nEnter text for the Text Analyzer: ")

# Save input
with open("input.txt", "w") as file:
    file.write(user_text)

# Read input
with open("input.txt", "r") as file:
    text = file.read()

# Total words
words = text.split()
total_words = len(words)

# Total characters
total_characters = len(text)

# Word frequency
word_frequency = {}

for word in words:
    word = word.lower().strip(string.punctuation)

    if word:
        word_frequency[word] = word_frequency.get(word, 0) + 1

# Display results
print("\n" + "=" * 40)
print("          TEXT ANALYZER")
print("=" * 40)

print(f"Total Words: {total_words}")
print(f"Total Characters: {total_characters}")

print("\nWord Frequency:")

for word, count in word_frequency.items():
    print(f"{word}: {count}")

# Save word frequency
with open("word_count.txt", "w") as file:
    for word, count in word_frequency.items():
        file.write(f"{word}: {count}\n")

print("\nWord frequency saved to word_count.txt")
print("=" * 40)


# ============================================================
# END OF DAY 14 SOLUTIONS
# ============================================================
