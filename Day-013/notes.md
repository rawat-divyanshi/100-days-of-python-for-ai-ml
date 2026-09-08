# Day 13: String Manipulation - Regular Expressions

## Topic 1: What is Regular Expressions (Regex)?

**Definition:** Regex is a way to find patterns in text instead of exact matches.

**Why use it?**
- Find all emails, phone numbers, dates
- Validate passwords, usernames
- Replace multiple text patterns at once
- Much easier than loops and conditions

**The re Module:**
```python
import re
```

**Main Methods:**
- `re.findall()` - Find ALL matches
- `re.search()` - Find FIRST match
- `re.sub()` - Replace text
- `re.match()` - Match at START only

---

## Topic 2: Basic Regex Patterns

**Character Patterns (What to find):**

| Pattern | Finds |
|---------|-------|
| `\d` | Any digit (0-9) |
| `\d+` | One or more digits grouped |
| `\D` | Non-digit (letters, symbols) |
| `\w` | Letters, digits, underscore |
| `\w+` | One or more word characters |
| `\W` | Non-word character |
| `\s` | Whitespace (spaces, tabs) |
| `\S` | Non-whitespace |
| `.` | Any character (except newline) |
| `[a-z]` | Lowercase letters |
| `[A-Z]` | Uppercase letters |
| `[a-zA-Z]` | Any letter |
| `[0-9]` | Any digit |

**Quantifiers (How many?):**

| Pattern | Means |
|---------|-------|
| `+` | 1 or more |
| `*` | 0 or more |
| `?` | 0 or 1 (optional) |
| `{3}` | Exactly 3 |
| `{2,4}` | Between 2 and 4 |

**Anchors (Position):**

| Pattern | Means |
|---------|-------|
| `^` | Start of string |
| `$` | End of string |

**Important Rule:**
- Always use raw strings: `r'\d+'` NOT `'\d+'`
- Escape special chars: `r'example\.com'` NOT `r'example.com'`

---

## Topic 3: re.findall() - Finding ALL Matches

**What it does:**
- Finds ALL patterns in text
- Returns a list of matches
- Returns empty list if no matches

**Syntax:**
```python
import re
result = re.findall(r'pattern', text)
```

**Example 1: Find all numbers**
```python
text = "I have 5 apples and 10 oranges"
result = re.findall(r'\d+', text)
# Output: ['5', '10']
```

**Example 2: Find all words**
```python
text = "Hello World Python"
result = re.findall(r'[a-zA-Z]+', text)
# Output: ['Hello', 'World', 'Python']
```

**Example 3: Find emails**
```python
text = "Contact john@example.com or jane@company.org"
result = re.findall(r'\w+@\w+\.\w+', text)
# Output: ['john@example.com', 'jane@company.org']
```

**Example 4: Find phone numbers**
```python
text = "Call 555-123-4567"
result = re.findall(r'\d{3}-\d{3}-\d{4}', text)
# Output: ['555-123-4567']
```

**Example 5: Find hashtags**
```python
text = "#python #AI #ML"
result = re.findall(r'#[a-zA-Z]+', text)
# Output: ['#python', '#AI', '#ML']
```

**Common Mistakes:**
1. Forgetting `r` prefix: `re.findall('\d+', text)` ❌
2. Not escaping dot: `r'example.com'` matches 'example com' ❌
3. No match returns `[]` not `None`

---

**Status: Topics 1-3 Complete ✓**