# Day 013 – String Manipulation Deep Dive Quiz

This quiz tests the concepts covered in **Day 13** of the 100 Days of Python for AI/ML challenge.

## Topics Covered

- Regular Expressions
- Python `re` module
- `re.search()`
- `re.match()`
- `re.findall()`
- `re.sub()`
- `re.split()`
- Basic Regular Expression patterns
- String formatting
- f-strings
- `.format()`
- Number formatting
- Percentage formatting
- Word counting
- Palindrome checking

---

# Multiple Choice Questions

## Q1. Which module is used for Regular Expressions in Python?

A. `regex`

B. `re`

C. `regexp`

D. `string`

---

## Q2. Which function searches for a pattern anywhere in a string?

A. `re.search()`

B. `re.find()`

C. `re.match()`

D. `re.scan()`

---

## Q3. What does `re.match()` do?

A. Searches the entire string

B. Searches only at the beginning of the string

C. Searches only at the end of the string

D. Replaces text

---

## Q4. What does `re.findall()` return?

A. The first match

B. A Boolean value

C. All matching occurrences

D. The last match

---

## Q5. What is the output?

```python
import re

text = "Python 123"

result = re.findall(r"\d+", text)

print(result)