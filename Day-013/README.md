# Day 013 – String Manipulation Deep Dive

Welcome to **Day 13** of my **100 Days of Python for AI/ML** challenge.

Today, I focused on working with strings at a deeper level by learning the basics of **Regular Expressions**, different **String Formatting techniques**, and practical **Text Processing** tasks.

---

## Topics Covered

### 1. Regular Expressions Basics

Learned the fundamentals of Python's `re` module for searching and processing text.

Topics covered:

- Introduction to Regular Expressions
- `import re`
- `re.search()`
- `re.match()`
- `re.findall()`
- `re.sub()`
- `re.split()`
- Raw strings
- Basic regex patterns
- `\d` – digits
- `\w` – word characters
- `\s` – whitespace
- `.` – any character
- `+` – one or more occurrences
- `*` – zero or more occurrences
- `?` – zero or one occurrence
- `^` – beginning of string
- `$` – end of string

Example:

```python
import re

text = "Python 123 is powerful"

numbers = re.findall(r"\d+", text)

print(numbers)