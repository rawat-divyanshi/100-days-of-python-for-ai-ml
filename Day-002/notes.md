# How Python Works

## 1. What is a Python Program?

A Python program is a collection of instructions written in the Python programming language to perform a specific task.

Example:

```python
print("Hello, World!")
```

When this program is executed, Python reads the instruction and displays the output on the screen.

---

## 2. What is a `.py` File?

A `.py` file is a file that contains Python source code.

Examples:

- hello.py
- calculator.py
- student.py
- main.py

Python programs are usually saved with the `.py` extension.

---

## 3. What is the Python Interpreter?

The Python Interpreter is a program that reads, translates, and executes Python code line by line.

It acts as a bridge between your Python code and the computer.

Flow:

```
You write Python code
        ↓
Save it as a .py file
        ↓
Python Interpreter reads the code
        ↓
The computer executes the instructions
        ↓
Output is displayed
```

---

## 4. How Python Executes Code

Python executes code from top to bottom, one line at a time.

Example:

```python
print("A")
print("B")
print("C")
```

Output:

```
A
B
C
```

Each statement is executed in order.

---

## 5. What Happens When an Error Occurs?

If Python encounters an unhandled error, it immediately stops execution.

Example:

```python
print("A")
print("B")
print(5/0)
print("C")
```

Output:

```
A
B

ZeroDivisionError: division by zero
```

Notice that `"C"` is never printed because execution stops at the error.

---

## 6. Key Points

- Python programs are stored in `.py` files.
- The Python Interpreter executes Python code.
- Python executes statements one by one.
- An unhandled error stops the program.
- Debugging means finding and fixing errors in code.