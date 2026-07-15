# Day 007 Quiz

## Multiple Choice Questions (MCQs)

### Q1. What is a Nested Loop?

A. A loop that never ends

B. A loop inside another loop

C. A loop with an if statement

D. A loop using range()

**Answer:** ________

---

### Q2. When does the `else` block of a loop execute?

A. When the loop starts

B. When the loop ends normally

C. When `break` is used

D. Never

**Answer:** ________

---

### Q3. Which statement prevents the loop `else` block from executing?

A. continue

B. pass

C. break

D. return

**Answer:** ________

---

### Q4. Which number is NOT a prime number?

A. 2

B. 5

C. 9

D. 13

**Answer:** ________

---

### Q5. What is the value of `5!`?

A. 20

B. 60

C. 120

D. 720

**Answer:** ________

---

# True or False

### Q6.

A nested loop means one loop inside another loop.

**Answer:** ________

---

### Q7.

The `else` block executes even if the loop is terminated using `break`.

**Answer:** ________

---

### Q8.

A prime number has exactly two factors.

**Answer:** ________

---

### Q9.

The Fibonacci Series starts with 0 and 1.

**Answer:** ________

---

### Q10.

Factorial uses repeated multiplication.

**Answer:** ________

---

# Short Answer Questions

### Q11.

What is a Nested Loop?

---

### Q12.

What is the purpose of the `else` clause in a loop?

---

### Q13.

Define a Prime Number.

---

### Q14.

What is a Factorial?

---

### Q15.

What is the Fibonacci Series?

---

# Predict the Output

### Q16.

```python
for i in range(3):
    for j in range(2):
        print("*", end="")
    print()
```

**Output:**

____________________

---

### Q17.

```python
for i in range(3):
    print(i)
else:
    print("Done")
```

**Output:**

____________________

---

### Q18.

```python
for i in range(5):

    if i == 2:
        break

    print(i)

else:
    print("Completed")
```

**Output:**

____________________

---

### Q19.

```python
fact = 1

for i in range(1, 5):
    fact *= i

print(fact)
```

**Output:**

____________________

---

### Q20.

```python
a = 0
b = 1

for i in range(5):
    print(a, end=" ")
    a, b = b, a + b
```

**Output:**

____________________

---

# Interview Questions

1. What is a Nested Loop?

2. Explain the difference between a single loop and a nested loop.

3. When is the `else` block of a loop executed?

4. Why doesn't the `else` block execute after a `break`?

5. What is a Prime Number?

6. How do you check whether a number is prime?

7. What is a Factorial? Give an example.

8. What is the Fibonacci Series?

9. Where are nested loops used in real-world programming?

10. What is the difference between `break`, `continue`, and `pass`?

---

# Debug the Code

Find and correct the mistake.

```python
number = 5
factorial = 0

for i in range(1, number + 1):
    factorial *= i

print(factorial)
```

What's wrong with this program?

____________________

---

# Challenge Question

Without running the program, predict the output.

```python
for i in range(1, 4):

    for j in range(i):
        print(i, end=" ")

    print()
```

**Output:**

____________________

---

# Coding Challenge

Write a Python program to:

- Ask the user to enter a number.
- Check whether it is a Prime Number.
- If it is prime, print:
  ```
  Prime Number
  ```
- Otherwise print:
  ```
  Not Prime Number
  ```

Try solving it without looking at `solutions.py`.

---

# Quick Revision

### Nested Loop

```
Loop
   ↓
Another Loop
```

---

### Loop with else

```
Loop Ends Normally
        ↓
else Executes
```

```
Loop Ends with break
        ↓
else Skipped
```

---

### Prime Number

- Exactly two factors
- 1 and itself

---

### Factorial

```
5!

↓

5 × 4 × 3 × 2 × 1

↓

120
```

---

### Fibonacci Series

```
0 1 1 2 3 5 8 13 ...
```

Next Number = Sum of Previous Two Numbers

---

## Day 007 Complete

If you can solve today's exercises and answer these questions confidently, you've taken another important step toward becoming a better problem solver and Python programmer.