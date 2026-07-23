"""
===========================================
Day 012 - Solutions
Topic: Dictionaries
Exercises 1 - 10
===========================================
"""

# ==========================================
# Exercise 1
# ==========================================

student = {}
print(student)


# ==========================================
# Exercise 2
# ==========================================

student = {
    "name": "Amit",
    "age": 23,
    "course": "Python"
}

print(student)


# ==========================================
# Exercise 3
# ==========================================

print(student["name"])


# ==========================================
# Exercise 4
# ==========================================

print(student.get("course"))


# ==========================================
# Exercise 5
# ==========================================

student["city"] = "Haridwar"

print(student)


# ==========================================
# Exercise 6
# ==========================================

student["age"] = 24

print(student)


# ==========================================
# Exercise 7
# ==========================================

print(student.keys())


# ==========================================
# Exercise 8
# ==========================================

print(student.values())


# ==========================================
# Exercise 9
# ==========================================

print(student.items())


# ==========================================
# Exercise 10
# ==========================================

if "email" in student:
    print("Email key exists.")
else:
    print("Email key does not exist.")

    """
===========================================
Day 012 - Solutions
Topic: Dictionaries
Exercises 11 - 20
===========================================
"""

# ==========================================
# Exercise 11
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "course": "Python",
    "city": "Haridwar"
}

student.pop("city")

print(student)


# ==========================================
# Exercise 12
# ==========================================

del student["course"]

print(student)


# ==========================================
# Exercise 13
# ==========================================

student.update({"country": "India"})

print(student)


# ==========================================
# Exercise 14
# ==========================================

marks = {
    "Amit": 90,
    "Rahul": 85,
    "Priya": 92,
    "Neha": 88,
    "Rohan": 95
}

print(marks)


# ==========================================
# Exercise 15
# ==========================================

highest = max(marks.values())

print("Highest Marks:", highest)


# ==========================================
# Exercise 16
# ==========================================

print("Student Names:")

for name in marks.keys():
    print(name)


# ==========================================
# Exercise 17
# ==========================================

print("Marks:")

for mark in marks.values():
    print(mark)


# ==========================================
# Exercise 18
# ==========================================

print("Student Records:")

for name, mark in marks.items():
    print(name, ":", mark)


# ==========================================
# Exercise 19
# ==========================================

squares = {x: x ** 2 for x in range(1, 11)}

print(squares)


# ==========================================
# Exercise 20
# ==========================================

even_cubes = {x: x ** 3 for x in range(1, 11) if x % 2 == 0}

print(even_cubes)

"""
===========================================
Day 012 - Solutions
Topic: Dictionaries
Exercises 21 - 25
Bonus Challenge
===========================================
"""

# ==========================================
# Exercise 21
# ==========================================

students = {
    "S101": {
        "name": "Amit",
        "marks": 90
    },
    "S102": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students)


# ==========================================
# Exercise 22
# ==========================================

print("Second Student Marks:")

print(students["S102"]["marks"])


# ==========================================
# Exercise 23
# ==========================================

text = "dictionary"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:")

for char, count in frequency.items():
    print(char, ":", count)


# ==========================================
# Exercise 24
# ==========================================

sentence = "python is easy and python is powerful"

words = sentence.split()

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word Frequency:")

for word, count in word_frequency.items():
    print(word, ":", count)


# ==========================================
# Exercise 25
# ==========================================

product = {
    "Product Name": "Laptop",
    "Price": 50000,
    "Quantity": 2
}

total_cost = product["Price"] * product["Quantity"]

print("Product Details:")

for key, value in product.items():
    print(key, ":", value)

print("Total Cost:", total_cost)


# ==========================================
# Bonus Challenge
# ==========================================

phone_book = {}

while True:

    print("\n===== Phone Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")

        phone_book[name] = number

        print("Contact Added Successfully!")

    elif choice == "2":

        name = input("Enter Name to Search: ")

        if name in phone_book:
            print(name, ":", phone_book[name])
        else:
            print("Contact Not Found.")

    elif choice == "3":

        name = input("Enter Name to Update: ")

        if name in phone_book:
            number = input("Enter New Number: ")
            phone_book[name] = number
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found.")

    elif choice == "4":

        name = input("Enter Name to Delete: ")

        if name in phone_book:
            del phone_book[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found.")

    elif choice == "5":

        if len(phone_book) == 0:
            print("Phone Book is Empty.")
        else:
            print("\nAll Contacts")
            for name, number in phone_book.items():
                print(name, ":", number)

    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice. Please Try Again.")


print("\nCongratulations! You have completed all Day 012 Dictionary exercises.")