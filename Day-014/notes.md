````
# Day 014 – File Handling

## 1. Opening Files

Python uses the `open()` function to open a file.

### Syntax

```python
open("filename", "mode")
````

### Example

```python
file = open("example.txt", "r")
```

### Common File Modes

| Mode | Meaning        |
| ---- | -------------- |
| `r`  | Read           |
| `w`  | Write          |
| `a`  | Append         |
| `r+` | Read and Write |

---

# 2. Reading Files

Python provides several methods for reading file contents.

## `read()`

Reads the complete file.

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

## `readline()`

Reads one line at a time.

```python
with open("example.txt", "r") as file:
    line = file.readline()
    print(line)
```

## `readlines()`

Reads all lines and returns them as a list.

```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

Example file:

```text
Python is easy.
Python is powerful.
Python is useful.
```

Using `readlines()`:

```python
[
    "Python is easy.\n",
    "Python is powerful.\n",
    "Python is useful.\n"
]
```

---

# 3. Writing to Files

The `w` mode is used to write data into a file.

```python
with open("example.txt", "w") as file:
    file.write("Hello Python")
```

### Important

`w` mode **overwrites existing content**.

For example, if the file contains:

```text
Hello
```

and we run:

```python
with open("example.txt", "w") as file:
    file.write("Python")
```

The file will contain:

```text
Python
```

The previous content is removed.

---

# 4. Appending to Files

The `a` mode is used to add new content at the end of a file.

```python
with open("example.txt", "a") as file:
    file.write("\nPython for AI/ML")
```

If the file originally contains:

```text
Hello Python
```

After appending:

```text
Hello Python
Python for AI/ML
```

Unlike `w`, append mode does not remove existing content.

---

# 5. Working with `.txt` Files

A `.txt` file stores plain text.

Example:

```text
Python is easy.
Python is powerful.
Python is useful.
```

Python can be used to:

* Read text files
* Write text files
* Append text
* Search text
* Count words
* Process text
* Analyze text

Example:

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

---

# 6. Working with `.csv` Files

CSV stands for:

**Comma-Separated Values**

CSV files are commonly used to store tabular data.

Example:

```text
Name,Age,Marks
Amit,25,85
Rahul,24,90
Priya,23,88
```

Python provides a built-in `csv` module for working with CSV files.

## Reading a CSV File

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['Name', 'Age', 'Marks']
['Amit', '25', '85']
['Rahul', '24', '90']
['Priya', '23', '88']
```

## Writing to a CSV File

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Amit", 25, 85])
    writer.writerow(["Rahul", 24, 90])
```

---

# 7. Context Managers

A context manager allows us to work with files safely.

Python commonly uses the `with` statement for file handling.

### Example

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

The file is automatically closed after the `with` block finishes.

### Why use `with`?

* Automatically closes the file
* Safer file handling
* Cleaner code
* Prevents forgetting to close the file

Without a context manager:

```python
file = open("example.txt", "r")

data = file.read()

file.close()
```

With a context manager:

```python
with open("example.txt", "r") as file:
    data = file.read()
```

The second approach is generally preferred.

---

# 8. File Modes Summary

| Mode | Purpose        |
| ---- | -------------- |
| `r`  | Read           |
| `w`  | Write          |
| `a`  | Append         |
| `r+` | Read and Write |

### Remember

```text
r → Read
w → Write
a → Add
```

---

# 9. Word Occurrence Counter

One important practice problem for Day 14 is:

**Read a text file and count how many times each word occurs.**

Suppose `text.txt` contains:

```text
python is easy
python is powerful
python is popular
```

Expected output:

```text
python: 3
is: 3
easy: 1
powerful: 1
popular: 1
```

### Step 1 – Read the File

```python
with open("text.txt", "r") as file:
    text = file.read()
```

### Step 2 – Split the Text into Words

```python
words = text.split()
```

### Step 3 – Create an Empty Dictionary

```python
word_count = {}
```

### Step 4 – Count Each Word

```python
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
```

### Step 5 – Display the Result

```python
print(word_count)
```

### Complete Program

```python
with open("text.txt", "r") as file:
    text = file.read()

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
```

---

# 10. Basic File Handling Flow

```text
Open File
    ↓
Read / Write / Append
    ↓
Process Data
    ↓
Close File
```

When using `with`:

```text
with open()
      ↓
Perform Operation
      ↓
File Automatically Closes
```

---

# 11. Important Methods

| Method        | Purpose             |
| ------------- | ------------------- |
| `open()`      | Opens a file        |
| `read()`      | Reads complete file |
| `readline()`  | Reads one line      |
| `readlines()` | Reads all lines     |
| `write()`     | Writes data         |
| `close()`     | Closes a file       |

---

# 12. Important Concepts to Remember

### `read()`

```python
file.read()
```

Reads the entire file.

### `readline()`

```python
file.readline()
```

Reads one line.

### `readlines()`

```python
file.readlines()
```

Reads all lines as a list.

### `write()`

```python
file.write("Hello")
```

Writes data into a file.

### `with`

```python
with open("file.txt", "r") as file:
    data = file.read()
```

Automatically handles closing the file.

---

# 13. File Handling and AI/ML

File handling is an important foundation for AI and Machine Learning.

Real-world data is often stored in files such as:

* `.csv`
* `.txt`
* `.json`
* Log files
* Configuration files

For example, a Machine Learning dataset may be stored as:

```text
students.csv
customers.csv
sales.csv
```

Python can read these files and process the data before applying libraries such as:

```text
NumPy
Pandas
Matplotlib
Scikit-learn
```

Therefore, file handling is an important step toward working with real-world datasets.

---

# 14. Day 14 Summary

Today we learned:

* How to open files
* How to read files
* How to write files
* How to append data
* How to work with `.txt` files
* How to work with `.csv` files
* How to use the `csv` module
* How to use context managers
* How to count word occurrences

---

# Key Takeaways

1. `open()` is used to open files.
2. `r` is used for reading.
3. `w` is used for writing and overwrites existing content.
4. `a` is used for appending.
5. `read()` reads the complete file.
6. `readline()` reads one line.
7. `readlines()` reads multiple lines.
8. `write()` writes data to a file.
9. `csv` is used to work with CSV files.
10. `with` automatically manages file closing.
11. File handling is an important skill for working with real-world AI/ML data.

```
```
