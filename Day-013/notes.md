# Day 13: String Manipulation & Regular Expressions - Complete Notes

## Table of Contents
1. What is Regular Expressions (Regex)?
2. Why Learn Regex?
3. Special Characters & Patterns
4. How to Use Regex in Python
5. Common Real-World Patterns
6. Advanced String Formatting
7. Common Mistakes & How to Avoid Them
8. Quick Reference

---

## 1. WHAT IS REGULAR EXPRESSIONS (REGEX)?

### Simple Definition
A **regular expression** is a pattern of text that helps you:
- FIND text matching a pattern
- REPLACE text matching a pattern
- VALIDATE if text matches a pattern
- EXTRACT data matching a pattern

### Real-World Analogy
Think of regex like a search filter:
- Google Search: "machine learning" finds all pages with those exact words
- Regex: `\d+` finds all numbers in text (any digit pattern)

### Without Regex vs With Regex

**WITHOUT REGEX (Complicated):**
```python
email = "john@example.com"

# Check if valid email (many conditions!)
if "@" in email and "." in email.split("@")[1]:
    if email.count("@") == 1:
        if len(email.split("@")[0]) > 0:
            print("Might be valid")
```

**WITH REGEX (Simple):**
```python
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.search(pattern, email):
    print("Valid email!")
```

---

## 2. WHY LEARN REGEX?

### Problem 1: Validating User Input
```
Scenario: Your app needs to check if users enter valid emails
Without Regex: 15-20 lines of complex code
With Regex: 1 pattern, 1 line of code
```

### Problem 2: Extracting Information
```
Scenario: Extract all phone numbers from a document
Without Regex: Loop through text, manually check each character
With Regex: re.findall(pattern) gets all matches instantly
```

### Problem 3: Text Cleaning
```
Scenario: Remove all special characters from text
Without Regex: Multiple replace() calls
With Regex: One re.sub() call
```

### Problem 4: Data Processing
```
Scenario: Find all URLs in a webpage
Without Regex: Complex string parsing
With Regex: Simple pattern match
```

**Conclusion:** Regex saves time, reduces errors, and makes code cleaner.

---

## 3. SPECIAL CHARACTERS & PATTERNS

### Basic Special Characters (The Building Blocks)

#### Character `.` (Dot)
```
Matches: Any single character EXCEPT newline
Pattern: a.b
Matches: "aab", "acb", "a1b", "a b"
Does NOT match: "ab" (needs exactly one character between a and b)
```

#### Quantifiers (How Many Times?)

**`+` (One or More)**
```
Pattern: a+
Matches: "a", "aa", "aaa", "aaaa"
Does NOT match: "" (needs at least one)
Use case: When you want at least 1 occurrence
```

**`*` (Zero or More)**
```
Pattern: a*b
Matches: "b", "ab", "aab", "aaab"
Does NOT match: nothing (it's flexible)
Use case: When something might not appear at all
```

**`?` (Zero or One - Optional)**
```
Pattern: colou?r
Matches: "color" (American), "colour" (British)
Does NOT match: "colouur"
Use case: Making something optional
```

**`{n}` (Exactly n Times)**
```
Pattern: \d{3}
Matches: "123", "456", "789"
Does NOT match: "12" or "1234"
Use case: Fixed length requirements
```

**`{n,m}` (Between n and m Times)**
```
Pattern: a{2,4}
Matches: "aa", "aaa", "aaaa"
Does NOT match: "a" or "aaaaa"
```

#### Anchors (Start & End)

**`^` (Start of String)**
```
Pattern: ^hello
Matches: "hello world" (at the beginning)
Does NOT match: "say hello" (hello not at start)
Use case: Ensure pattern is at the beginning
```

**`$` (End of String)**
```
Pattern: world$
Matches: "hello world" (at the end)
Does NOT match: "world map" (world not at end)
Use case: Ensure pattern is at the ending
```

**`\b` (Word Boundary)**
```
Pattern: \bcat\b
Matches: "the cat sat" (cat as complete word)
Does NOT match: "concatenate" (cat is part of word)
Use case: Match complete words only
```

#### Character Classes `[ ]` (Choose One)

**Simple Character Class**
```
Pattern: [aeiou]
Matches: Any single vowel
Matches: "apple" (finds 'a'), "egg" (finds 'e')
Use case: Match any character from a set
```

**Range in Character Class**
```
Pattern: [a-z]
Matches: Any lowercase letter (a through z)

Pattern: [A-Z]
Matches: Any uppercase letter

Pattern: [0-9]
Matches: Any digit

Pattern: [a-zA-Z0-9]
Matches: Letters or digits
```

**Negation in Character Class**
```
Pattern: [^0-9]
Matches: Anything that is NOT a digit
Matches: "a", "!", "@", " " (space)
Does NOT match: "5"
Use case: Exclude certain characters
```

#### OR (`|`)
```
Pattern: cat|dog
Matches: Either "cat" OR "dog"
Matches: "I have a cat", "I have a dog"
Use case: Multiple alternatives
```

### Special Sequences (Shortcuts)

These are abbreviations for common patterns:

```
\d   = [0-9]           (any digit)
\D   = [^0-9]          (any non-digit)
\w   = [a-zA-Z0-9_]    (word character: letters, digits, underscore)
\W   = [^\w]           (non-word character)
\s   = whitespace      (space, tab, newline)
\S   = non-whitespace
.    = any character   (except newline)
```

### Examples Using Special Sequences

```python
import re

# \d finds digits
text = "I have 2 cats and 3 dogs"
numbers = re.findall(r'\d', text)
# Result: ['2', '3']

# \w finds word characters
text = "hello123_world!"
matches = re.findall(r'\w', text)
# Result: ['h','e','l','l','o','1','2','3','_','w','o','r','l','d']

# \s finds whitespace
text = "hello   world"
spaces = re.findall(r'\s', text)
# Result: [' ', ' ', ' ']

# \S finds non-whitespace
text = "hello world"
non_spaces = re.findall(r'\S+', text)
# Result: ['hello', 'world']
```

---

## 4. HOW TO USE REGEX IN PYTHON

### Import the Module
```python
import re
```

### Method 1: `re.search()` - Find First Match

**What it does:** Finds the FIRST match, returns None if not found

**Syntax:**
```python
match = re.search(pattern, text)
if match:
    print(match.group())  # Get the matched text
```

**Example:**
```python
import re

text = "My phone is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'

match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")
    print(f"Position: {match.start()}-{match.end()}")
    
# Output:
# Found: 123-456-7890
# Position: 13-25
```

**When to use:** When you only need the first match

---

### Method 2: `re.findall()` - Find All Matches

**What it does:** Returns a LIST of ALL matches

**Syntax:**
```python
matches = re.findall(pattern, text)
# Returns a list
```

**Example:**
```python
import re

text = "Call 123-456-7890 or 987-654-3210"
pattern = r'\d{3}-\d{3}-\d{4}'

matches = re.findall(pattern, text)
print(matches)
# Output: ['123-456-7890', '987-654-3210']

# Loop through all matches
for phone in matches:
    print(f"Phone: {phone}")
```

**When to use:** When you need to find ALL occurrences

---

### Method 3: `re.sub()` - Replace Matches

**What it does:** Replaces all matches with a replacement string

**Syntax:**
```python
result = re.sub(pattern, replacement, text)
```

**Example 1: Simple Replacement**
```python
import re

text = "I have 2 apples and 3 oranges"
result = re.sub(r'\d', 'X', text)
print(result)
# Output: "I have X apples and X oranges"

# Explanation:
# \d matches each digit
# 'X' replaces each digit
```

**Example 2: Replace Only First N Matches**
```python
import re

text = "apple orange apple banana apple"
# Replace only first 2 occurrences
result = re.sub(r'apple', 'fruit', text, count=2)
print(result)
# Output: "fruit orange fruit banana apple"
```

**When to use:** When you need to replace patterns (hiding info, cleaning data)

---

### Method 4: `re.split()` - Split by Pattern

**What it does:** Splits text by a pattern instead of a fixed separator

**Syntax:**
```python
parts = re.split(pattern, text)
```

**Example 1: Split by Multiple Separators**
```python
import re

text = "apple, banana; orange: grape"
# Split by comma, semicolon, or colon
result = re.split(r'[,;:]', text)
print(result)
# Output: ['apple', ' banana', ' orange', ' grape']
```

**Example 2: Split by Whitespace**
```python
import re

text = "hello    world    python"
# \s+ means one or more whitespace
result = re.split(r'\s+', text)
print(result)
# Output: ['hello', 'world', 'python']
```

**When to use:** When you need to split by complex patterns

---

### Method 5: `re.finditer()` - Find With Positions

**What it does:** Returns iterator with each match AND its position

**Syntax:**
```python
for match in re.finditer(pattern, text):
    print(match.group())      # The matched text
    print(match.start())      # Start position
    print(match.end())        # End position
```

**Example:**
```python
import re

text = "Emails: john@gmail.com and sarah@yahoo.com"
pattern = r'[\w.-]+@[\w.-]+'

for match in re.finditer(pattern, text):
    print(f"Email: {match.group()}")
    print(f"Position: {match.start()}-{match.end()}")

# Output:
# Email: john@gmail.com
# Position: 8-22
# Email: sarah@yahoo.com
# Position: 27-42
```

**When to use:** When you need both the match AND its position

---

## 5. COMMON REAL-WORLD PATTERNS

### Pattern 1: Email Validation

**Understanding the Pattern:**
```
^                          = Start of string
[a-zA-Z0-9._%+-]+         = Username (letters, numbers, dot, %, +, -)
@                         = Literal @ symbol
[a-zA-Z0-9.-]+            = Domain name
\.                        = Literal dot (must escape with \)
[a-zA-Z]{2,}              = Extension (2+ letters like .com, .org)
$                         = End of string
```

**Full Pattern:**
```python
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

**Usage:**
```python
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.search(pattern, email))

# Test:
print(is_valid_email("john@gmail.com"))      # True
print(is_valid_email("sarah@yahoo.co.uk"))   # True
print(is_valid_email("invalid.email"))       # False
print(is_valid_email("test@.com"))           # False
```

---

### Pattern 2: Phone Number (XXX-XXX-XXXX)

**Understanding the Pattern:**
```
^            = Start
\d{3}        = Exactly 3 digits
-            = Literal dash
\d{3}        = Exactly 3 digits
-            = Literal dash
\d{4}        = Exactly 4 digits
$            = End
```

**Full Pattern:**
```python
pattern = r'^\d{3}-\d{3}-\d{4}$'
```

**Usage:**
```python
import re

def is_valid_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.search(pattern, phone))

print(is_valid_phone("123-456-7890"))   # True
print(is_valid_phone("1234567890"))     # False (no dashes)
print(is_valid_phone("123-45-6789"))    # False (wrong format)
```

---

### Pattern 3: URL/Website

**Understanding the Pattern:**
```
https?       = http or https (? makes 's' optional)
://          = Literal "://"
[\w.-]+      = Domain name (letters, numbers, dots, hyphens)
\.           = Literal dot
[a-zA-Z]{2,} = Extension (.com, .org, .co.uk, etc)
```

**Full Pattern:**
```python
pattern = r'https?://[\w.-]+\.[a-zA-Z]{2,}'
```

**Usage:**
```python
import re

text = "Visit https://python.org and http://github.com"
urls = re.findall(r'https?://[\w.-]+\.[a-zA-Z]{2,}', text)
print(urls)
# Output: ['https://python.org', 'http://github.com']
```

---

### Pattern 4: Find Complete Words

**Understanding the Pattern:**
```
\b      = Word boundary (start or end of word)
\w+     = One or more word characters
\b      = Word boundary
```

**Full Pattern:**
```python
pattern = r'\b\w+\b'
```

**Usage:**
```python
import re

text = "hello123 world test_case"
words = re.findall(r'\b\w+\b', text)
print(words)
# Output: ['hello123', 'world', 'test_case']
```

---

### Pattern 5: Find Numbers (Including Decimals & Negatives)

**Understanding the Pattern:**
```
-?       = Optional minus sign
\d+      = One or more digits
\.?      = Optional dot
\d*      = Zero or more decimal digits
```

**Full Pattern:**
```python
pattern = r'-?\d+\.?\d*'
```

**Usage:**
```python
import re

text = "Temps: 25, -3.5, 0, 98.6, -10"
numbers = re.findall(r'-?\d+\.?\d*', text)
print(numbers)
# Output: ['25', '-3.5', '0', '98.6', '-10']
```

---

### Pattern 6: Hashtags

**Understanding the Pattern:**
```
#       = Literal hash symbol
\w+     = One or more word characters (letters, digits, underscore)
```

**Full Pattern:**
```python
pattern = r'#\w+'
```

**Usage:**
```python
import re

text = "Love #Python #coding #ML!"
tags = re.findall(r'#\w+', text)
print(tags)
# Output: ['#Python', '#coding', '#ML']
```

---

### Pattern 7: Mentions (@username)

**Understanding the Pattern:**
```
@       = Literal @ symbol
\w+     = Username (word characters)
```

**Full Pattern:**
```python
pattern = r'@\w+'
```

**Usage:**
```python
import re

text = "Hey @john and @sarah, check this out!"
mentions = re.findall(r'@\w+', text)
print(mentions)
# Output: ['@john', '@sarah']
```

---

## 6. ADVANCED STRING FORMATTING

### F-Strings (Recommended - Modern & Easiest)

**Basic Syntax:**
```python
name = "Alice"
age = 25

print(f"Hello, {name}!")
# Output: Hello, Alice!

print(f"Next year: {age + 1}")
# Output: Next year: 26
```

**Formatting Numbers:**
```python
price = 19.99
count = 5

# 2 decimal places
print(f"Price: ${price:.2f}")
# Output: Price: $19.99

# No decimals
print(f"Count: {count:.0f}")
# Output: Count: 5

# Percentage
percentage = 0.75
print(f"Progress: {percentage:.1%}")
# Output: Progress: 75.0%

# Thousands separator
big_num = 1000000
print(f"Population: {big_num:,}")
# Output: Population: 1,000,000
```

**Fixed Width:**
```python
name1 = "Bob"
name2 = "Alice"

# 10 characters wide
print(f"Name: {name1:10} Age: {age:3d}")
print(f"Name: {name2:10} Age: {age:3d}")

# Output:
# Name: Bob        Age: 25
# Name: Alice      Age: 25
```

---

### .format() Method (Traditional)

**Basic Syntax:**
```python
name = "Bob"
age = 30

print("My name is {}".format(name))
# Output: My name is Bob

print("{} is {} years old".format(name, age))
# Output: Bob is 30 years old
```

**Named Placeholders:**
```python
print("{name} is {age} years old".format(name="Bob", age=30))
# Output: Bob is 30 years old
```

---

### % Operator (Old Style - Still Works)

**Syntax:**
```python
name = "Charlie"
age = 35

print("Name: %s, Age: %d" % (name, age))
# Output: Name: Charlie, Age: 35

# %s = string
# %d = integer
# %f = float
```

---

## 7. COMMON MISTAKES & HOW TO AVOID THEM

### Mistake 1: Forgetting Raw String (r'')

**WRONG:**
```python
pattern = '\d+'  # Python interprets \d as something else
```

**RIGHT:**
```python
pattern = r'\d+'  # Raw string preserves backslash
```

**Why:** In regular strings, backslash is an escape character. Use raw strings (r'') for regex patterns.

---

### Mistake 2: Using `.` Without Escaping

**WRONG:**
```python
pattern = r'gmail.com'  # . matches ANY character
# Matches: "gmailXcom", "gmail9com"
```

**RIGHT:**
```python
pattern = r'gmail\.com'  # \. is literal dot
# Matches only: "gmail.com"
```

---

### Mistake 3: Confusing re.search() and re.findall()

**WRONG:**
```python
matches = re.search(r'\d+', "abc 123 def 456")
# Returns only: 123 (first match)

for match in matches:  # ERROR! Can't loop over single match
    print(match)
```

**RIGHT:**
```python
matches = re.findall(r'\d+', "abc 123 def 456")
# Returns: ['123', '456'] (all matches)

for match in matches:  # Works!
    print(match)
```

---

### Mistake 4: Forgetting Escaping Special Characters

**WRONG:**
```python
pattern = r'(abc)'  # ( ) are special characters
# This groups "abc" instead of matching literal parentheses
```

**RIGHT:**
```python
pattern = r'\(abc\)'  # Escape with backslash
# Matches literal: (abc)
```

---

## 8. QUICK REFERENCE

### All Regex Methods

| Method | Purpose | Returns |
|--------|---------|---------|
| `re.search(pattern, text)` | Find first match | Match object or None |
| `re.findall(pattern, text)` | Find all matches | List of matches |
| `re.sub(pattern, replace, text)` | Replace matches | Modified string |
| `re.split(pattern, text)` | Split by pattern | List of parts |
| `re.finditer(pattern, text)` | Find all with positions | Iterator |

### Common Patterns Quick Table

| Pattern | Matches | Example |
|---------|---------|---------|
| `\d` | Any digit | "123" |
| `\d+` | One or more digits | "123" |
| `\w` | Word character | "a", "1", "_" |
| `\s` | Whitespace | " ", "\t" |
| `.` | Any character | "x" |
| `+` | One or more | "aaa" from pattern `a+` |
| `*` | Zero or more | "aaa" or "" from pattern `a*` |
| `?` | Optional | "color" or "colour" |
| `{3}` | Exactly 3 | "aaa" from pattern `a{3}` |
| `^` | Start of string | "^hello" matches "hello world" |
| `$` | End of string | "world$" matches "hello world" |
| `[abc]` | Any of a, b, c | "a", "b", or "c" |
| `[a-z]` | Range a to z | Any lowercase letter |
| `[^0-9]` | Not a digit | Any non-digit |
| `\|` | OR | "cat\|dog" matches "cat" or "dog" |

### Practical Pattern Library

```python
import re

# Email
r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Phone (123-456-7890)
r'^\d{3}-\d{3}-\d{4}$'

# URL
r'https?://[\w.-]+\.[a-zA-Z]{2,}'

# Hashtag
r'#\w+'

# Mention
r'@\w+'

# Numbers (including decimals)
r'-?\d+\.?\d*'

# Words only
r'\b[a-z]+\b'

# Remove extra spaces
text = re.sub(r'\s+', ' ', text)

# Remove special characters
text = re.sub(r'[^a-zA-Z0-9]', '', text)

# Extract digits only
digits = re.findall(r'\d+', text)
```

---

## SUMMARY & KEY TAKEAWAYS

✅ **Regex is powerful** for text processing and validation  
✅ **Always use raw strings** (r'pattern') in Python  
✅ **Start simple, build complexity** gradually  
✅ **Test patterns online** at regex101.com  
✅ **Comment your regex** patterns in code  
✅ **Use re.findall()** when you need all matches  
✅ **Use re.sub()** when you need to replace  
✅ **Use re.search()** to check if pattern exists  
✅ **Escape special characters** with backslash (\)  
✅ **Practice regularly** to master patterns  

---

**Ready to practice? Move on to exercises!** 🚀
