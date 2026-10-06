````markdown
# Day 14 – File Handling Quiz

## Instructions

- Total Questions: 30
- Choose the best answer for each question.
- Try to solve the quiz without checking the answer key.
- Topics covered:
  - Opening files
  - Reading files
  - Writing files
  - Appending files
  - `.txt` files
  - `.csv` files
  - Context managers
  - Word occurrence counting

---

## Section 1 – Opening & Reading Files

### Q1. Which function is used to open a file in Python?

A. `file()`

B. `open()`

C. `read()`

D. `load()`

---

### Q2. Which mode opens a file for reading?

A. `w`

B. `a`

C. `r`

D. `x`

---

### Q3. What does the following code do?

```python
file = open("data.txt", "r")
````

A. Creates a new file only

B. Opens `data.txt` for reading

C. Opens `data.txt` for writing

D. Deletes `data.txt`

---

### Q4. Which method reads the entire contents of a file?

A. `read()`

B. `readline()`

C. `readlines()`

D. `readall()`

---

### Q5. Which method reads one line from a file?

A. `read()`

B. `readline()`

C. `readlines()`

D. `line()`

---

### Q6. What does `readlines()` return?

A. A single string

B. An integer

C. A list containing the lines of the file

D. A dictionary

---

### Q7. Suppose `data.txt` contains:

```text
Python is easy
Python is powerful
```

What will `file.read()` return?

A. `Python`

B. `Python is easy`

C. The complete file content

D. A list of words

---

### Q8. What happens if you try to open a file that does not exist using mode `"r"`?

A. Python automatically creates the file

B. Python deletes the file

C. Python raises a `FileNotFoundError`

D. Python returns `None`

---

## Section 2 – Writing & Appending Files

### Q9. Which mode is used for writing to a file?

A. `r`

B. `w`

C. `a`

D. `read`

---

### Q10. What happens when an existing file is opened using `"w"` mode?

A. Existing content can be overwritten

B. Existing content is always preserved

C. The file becomes read-only

D. The file is converted to CSV

---

### Q11. Which mode is used to append content to the end of a file?

A. `r`

B. `w`

C. `a`

D. `e`

---

### Q12. Consider:

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

What will happen if `notes.txt` already contains:

```text
Hello
```

A. The file becomes `HelloPython`

B. The file becomes `Python`

C. The file becomes empty

D. Python raises an error

---

### Q13. Consider:

```python
with open("notes.txt", "a") as file:
    file.write("Python")
```

What is the purpose of `"a"` mode?

A. Read the file

B. Delete the file

C. Add content to the existing file

D. Rename the file

---

### Q14. Which method is used to write a string into a file?

A. `write()`

B. `printfile()`

C. `insert()`

D. `appendfile()`

---

### Q15. Which code correctly writes `"Hello Python"` into `message.txt`?

A.

```python
open("message.txt", "r").write("Hello Python")
```

B.

```python
open("message.txt", "w").write("Hello Python")
```

C.

```python
open("message.txt", "a").read("Hello Python")
```

D.

```python
open("message.txt").write("Hello Python")
```

---

## Section 3 – Context Managers

### Q16. Which keyword is commonly used with files to create a context manager?

A. `for`

B. `with`

C. `using`

D. `file`

---

### Q17. What is the main advantage of using:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

A. The file is automatically closed after the block

B. The file is automatically converted to CSV

C. The file is permanently stored in memory

D. The file cannot contain spaces

---

### Q18. Which statement is correct about a context manager?

A. It automatically manages resources such as open files

B. It only works with CSV files

C. It can only be used for writing files

D. It permanently keeps the file open

---

### Q19. Which is the recommended modern style for reading a file?

A.

```python
file = open("data.txt", "r")
data = file.read()
```

B.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

C.

```python
read("data.txt")
```

D.

```python
file.read("data.txt")
```

---

## Section 4 – TXT & CSV Files

### Q20. What does `.txt` generally represent?

A. A text file

B. A Python program

C. A database

D. An image file

---

### Q21. Which Python module is commonly used to work with CSV files?

A. `data`

B. `table`

C. `csv`

D. `filedata`

---

### Q22. Which function is commonly used to read rows from a CSV file?

A. `csv.reader()`

B. `csv.readfile()`

C. `csv.rows()`

D. `csv.open()`

---

### Q23. Which function is commonly used to write rows into a CSV file?

A. `csv.write()`

B. `csv.writer()`

C. `csv.add()`

D. `csv.insert()`

---

### Q24. A CSV file commonly stores data in which structure?

A. Rows and columns separated by delimiters

B. Only images

C. Only Python functions

D. Binary machine code

---

## Section 5 – Word Counting & Text Processing

### Q25. Suppose:

```text
Python is easy
Python is powerful
Python is popular
```

How many times does `Python` occur?

A. 1

B. 2

C. 3

D. 4

---

### Q26. Which Python method can be used to split a sentence into words?

A. `split()`

B. `divide()`

C. `words()`

D. `separate()`

---

### Q27. What is the output of:

```python
text = "Python is easy"
words = text.split()

print(len(words))
```

A. `2`

B. `3`

C. `4`

D. `13`

---

### Q28. Which data structure is particularly useful for storing word frequencies?

A. List

B. Tuple

C. Dictionary

D. String

---

### Q29. Consider:

```python
text = "python is easy python is powerful"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency["python"])
```

What is the output?

A. `1`

B. `2`

C. `3`

D. `4`

---

### Q30. What is the correct general flow for a word occurrence counter using a text file?

A. Delete → Write → Close → Count

B. Open → Read → Process → Count → Display

C. Write → Delete → Read → Count

D. Close → Open → Delete → Display

---

# Answer Key

| Question | Answer |
| -------- | ------ |
| 1        | B      |
| 2        | C      |
| 3        | B      |
| 4        | A      |
| 5        | B      |
| 6        | C      |
| 7        | C      |
| 8        | C      |
| 9        | B      |
| 10       | A      |
| 11       | C      |
| 12       | B      |
| 13       | C      |
| 14       | A      |
| 15       | B      |
| 16       | B      |
| 17       | A      |
| 18       | A      |
| 19       | B      |
| 20       | A      |
| 21       | C      |
| 22       | A      |
| 23       | B      |
| 24       | A      |
| 25       | C      |
| 26       | A      |
| 27       | B      |
| 28       | C      |
| 29       | B      |
| 30       | B      |

---

# Score Guide

| Score | Level               |
| ----- | ------------------- |
| 27–30 | Excellent           |
| 23–26 | Very Good           |
| 18–22 | Good                |
| 12–17 | Needs Revision      |
| 0–11  | Revise Day 14 Again |

---

# Revision Checklist

Before moving to Day 15, make sure you can:

* [ ] Open a file using `open()`
* [ ] Understand `r`, `w`, and `a` modes
* [ ] Read a complete file using `read()`
* [ ] Read one line using `readline()`
* [ ] Read multiple lines using `readlines()`
* [ ] Write content using `write()`
* [ ] Append content using `"a"` mode
* [ ] Use `with open()` correctly
* [ ] Explain why context managers are useful
* [ ] Work with `.txt` files
* [ ] Read CSV files using `csv.reader`
* [ ] Write CSV files using `csv.writer`
* [ ] Count words in a text file
* [ ] Count word occurrences using a dictionary

---

# Day 14 Complete

**Topic:** File Handling

**Main Skills:**
File Reading + File Writing + File Appending + TXT + CSV + Context Managers + Word Occurrence Counting

```
```
