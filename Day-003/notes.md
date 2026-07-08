# Day 003 – Operators in Python

## Introduction

Operators are special symbols that perform operations on one or more values (called operands). They are one of the fundamental building blocks of programming and are used in almost every Python program.

Example:

```python
print(10 + 5)
```

Here:

* `10` and `5` are **operands**
* `+` is the **operator**

Output:

```
15
```

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name                | Example   | Output |
| -------- | ------------------- | --------- | -----: |
| `+`      | Addition            | `10 + 5`  |     15 |
| `-`      | Subtraction         | `10 - 5`  |      5 |
| `*`      | Multiplication      | `10 * 5`  |     50 |
| `/`      | Division            | `10 / 5`  |    2.0 |
| `%`      | Modulus (Remainder) | `10 % 3`  |      1 |
| `//`     | Floor Division      | `10 // 3` |      3 |
| `**`     | Exponent (Power)    | `2 ** 3`  |      8 |

Example:

```python
a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** 2)
```

---

# 2. Comparison Operators

Comparison operators compare two values and always return either `True` or `False`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

```python
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

Output:

```
False
True
True
False
True
False
```

---

# 3. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning                                        |
| -------- | ---------------------------------------------- |
| `and`    | Returns True if both conditions are True       |
| `or`     | Returns True if at least one condition is True |
| `not`    | Reverses the result                            |

Example:

```python
age = 20

print(age > 18 and age < 30)
print(age > 18 or age > 50)
print(not(age > 18))
```

---

# 4. Assignment Operators

Assignment operators are used to assign and update variable values.

| Operator | Example  | Equivalent To |
| -------- | -------- | ------------- |
| `=`      | `x = 5`  | Assign value  |
| `+=`     | `x += 2` | `x = x + 2`   |
| `-=`     | `x -= 2` | `x = x - 2`   |
| `*=`     | `x *= 2` | `x = x * 2`   |
| `/=`     | `x /= 2` | `x = x / 2`   |
| `%=`     | `x %= 2` | `x = x % 2`   |

Example:

```python
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)
```

---

# 5. Bitwise Operators (Basic Understanding)

Bitwise operators work directly on the binary representation (bits) of numbers.

| Operator | Meaning     |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left Shift  |            |
| `>>`     | Right Shift |            |

Example:

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```

**Note:** Bitwise operators are an advanced topic. At this stage, understanding what they are and where they are used is enough.

---

# 6. Operator Precedence

Operator precedence determines the order in which operations are performed.

Example:

```python
print(5 + 2 * 3)
```

Output:

```
11
```

Explanation:

```
2 × 3 = 6
5 + 6 = 11
```

Example:

```python
print((5 + 2) * 3)
```

Output:

```
21
```

Parentheses have the highest priority.

---

# Real-Life Example: Simple Calculator

```python
num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

# Key Points

* Operators perform operations on values.
* Arithmetic operators are used for calculations.
* Comparison operators return `True` or `False`.
* Logical operators combine conditions.
* Assignment operators update variable values.
* Bitwise operators work with binary numbers.
* Operator precedence decides the order of execution.
* Parentheses can be used to change the order of evaluation.

---

# Summary

In this lesson, you learned the different types of Python operators, including arithmetic, comparison, logical, assignment, and bitwise operators. You also learned how operator precedence affects the order of execution and how these operators can be used to build a simple calculator.
