# Day 13: String Manipulation - Regular Expressions
# PRACTICE PROBLEMS (Complete Mini-Projects)

import re
from collections import Counter

# ==========================================
# PRACTICE 1: Word Counter
# ==========================================

def word_counter(text):
    """
    Count frequency of each word in text.
    - Case insensitive
    - Ignore punctuation
    - Return dictionary with word counts
    """
    # Convert to lowercase
    text = text.lower()
    
    # Extract only words (letters only)
    words = re.findall(r'[a-z]+', text)
    
    # Count frequency
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts


# Test Practice 1
print("=== PRACTICE 1: Word Counter ===")
text1 = "The quick brown fox jumps over the lazy dog. The dog was lazy."
result1 = word_counter(text1)
print(f"Text: {text1}")
print(f"Word Counts: {result1}")
print(f"Most common word: {max(result1, key=result1.get)} appears {max(result1.values())} times")
print()


# ==========================================
# PRACTICE 2: Palindrome Checker
# ==========================================

def is_palindrome(text):
    """
    Check if text is a palindrome.
    - Ignore spaces and punctuation
    - Case insensitive
    - Return True/False
    """
    # Keep only alphanumeric characters, convert to lowercase
    cleaned = ''.join(re.findall(r'[a-z0-9]', text.lower()))
    
    # Check if same forwards and backwards
    return cleaned == cleaned[::-1]


# Test Practice 2
print("=== PRACTICE 2: Palindrome Checker ===")
test_cases_2 = [
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Madam",
    "12321",
    "python"
]
for test in test_cases_2:
    result = is_palindrome(test)
    print(f"'{test}' is palindrome: {result}")
print()


# ==========================================
# PRACTICE 3: Email Validator
# ==========================================

def is_valid_email(email):
    """
    Validate if string is a valid email.
    Pattern: username@domain.extension
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Test Practice 3
print("=== PRACTICE 3: Email Validator ===")
test_emails = [
    "john@example.com",
    "jane.doe@company.co.uk",
    "invalid.email@",
    "notanemail",
    "user@domain",
    "test@test.org",
    "admin_123@mysite.com"
]
for email in test_emails:
    result = is_valid_email(email)
    print(f"{email}: {result}")
print()


# ==========================================
# PRACTICE 4: Phone Number Extractor
# ==========================================

def extract_phone_numbers(text):
    """
    Extract all phone numbers in various formats:
    - XXX-XXX-XXXX
    - (XXX) XXX-XXXX
    - XXXXXXXXXX
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)


# Test Practice 4
print("=== PRACTICE 4: Phone Number Extractor ===")
text4 = """
Call sales at 555-123-4567 or (555) 987-6543.
My cell: 5551234567
Emergency: 911
Fax: (666) 789-0123
"""
result4 = extract_phone_numbers(text4)
print(f"Text: {text4}")
print(f"Phone Numbers Found: {result4}")
print()


# ==========================================
# PRACTICE 5: URL Extractor
# ==========================================

def extract_urls(text):
    """
    Extract all URLs from text.
    Supports: http://, https://
    """
    pattern = r'https?://[a-zA-Z0-9.-]+'
    return re.findall(pattern, text)


# Test Practice 5
print("=== PRACTICE 5: URL Extractor ===")
text5 = "Visit https://google.com or http://example.org or https://github.com/user"
result5 = extract_urls(text5)
print(f"Text: {text5}")
print(f"URLs Found: {result5}")
print()


# ==========================================
# PRACTICE 6: Hashtag Finder
# ==========================================

def find_hashtags(text):
    """
    Find all hashtags in text.
    Returns list of hashtags without duplicates.
    """
    hashtags = re.findall(r'#[a-zA-Z0-9_]+', text)
    return list(set(hashtags))  # Remove duplicates


# Test Practice 6
print("=== PRACTICE 6: Hashtag Finder ===")
text6 = "#python is great! #AI #MachineLearning #python #DataScience"
result6 = find_hashtags(text6)
print(f"Text: {text6}")
print(f"Hashtags Found: {result6}")
print()


# ==========================================
# PRACTICE 7: Text Cleaner (Remove Extra Spaces)
# ==========================================

def clean_text(text):
    """
    Clean text by removing extra spaces.
    Replace multiple spaces with single space.
    """
    return re.sub(r'\s+', ' ', text).strip()


# Test Practice 7
print("=== PRACTICE 7: Text Cleaner ===")
text7 = "Hello    world  this   has   extra     spaces"
result7 = clean_text(text7)
print(f"Original: '{text7}'")
print(f"Cleaned: '{result7}'")
print()


# ==========================================
# PRACTICE 8: Extract Numbers and Sum Them
# ==========================================

def sum_all_numbers(text):
    """
    Extract all numbers from text and return their sum.
    """
    numbers = re.findall(r'\d+', text)
    numbers = [int(n) for n in numbers]
    return sum(numbers)


# Test Practice 8
print("=== PRACTICE 8: Sum All Numbers ===")
text8 = "I have 5 apples, 10 oranges, and 3 bananas. Total: 18"
result8 = sum_all_numbers(text8)
print(f"Text: {text8}")
print(f"Sum of all numbers: {result8}")
print()


# ==========================================
# PRACTICE 9: Extract Email Domains
# ==========================================

def extract_domains(text):
    """
    Extract domain names from email addresses.
    Example: john@example.com → example.com
    """
    emails = re.findall(r'\w+@([\w.]+)', text)
    return emails


# Test Practice 9
print("=== PRACTICE 9: Extract Domains from Emails ===")
text9 = "Contact: john@gmail.com, jane@company.org, admin@github.io"
result9 = extract_domains(text9)
print(f"Text: {text9}")
print(f"Domains: {result9}")
print()


# ==========================================
# PRACTICE 10: Password Strength Checker
# ==========================================

def check_password_strength(password):
    """
    Check password strength based on:
    - Minimum 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    - Contains special character
    """
    issues = []
    
    if len(password) < 8:
        issues.append("Too short (min 8 chars)")
    
    if not re.search(r'[A-Z]', password):
        issues.append("Missing uppercase letter")
    
    if not re.search(r'[a-z]', password):
        issues.append("Missing lowercase letter")
    
    if not re.search(r'\d', password):
        issues.append("Missing digit")
    
    if not re.search(r'[!@#$%^&*]', password):
        issues.append("Missing special character")
    
    if len(issues) == 0:
        return "Strong", []
    else:
        return "Weak", issues


# Test Practice 10
print("=== PRACTICE 10: Password Strength Checker ===")
test_passwords = [
    "abc123",
    "Password1!",
    "password123",
    "PASSWORD123!",
    "P@ss123"
]
for pwd in test_passwords:
    strength, issues = check_password_strength(pwd)
    print(f"Password: '{pwd}' → Strength: {strength}")
    if issues:
        print(f"  Issues: {', '.join(issues)}")
print()


# ==========================================
# PRACTICE 11: Extract and Format Phone Numbers
# ==========================================

def format_phone_number(phone):
    """
    Extract digits from any phone format and format as (XXX) XXX-XXXX
    """
    # Extract only digits
    digits = re.findall(r'\d', phone)
    digits_str = ''.join(digits)
    
    # Format if we have 10 digits
    if len(digits_str) == 10:
        return f"({digits_str[:3]}) {digits_str[3:6]}-{digits_str[6:]}"
    else:
        return "Invalid phone number"


# Test Practice 11
print("=== PRACTICE 11: Format Phone Numbers ===")
test_phones = [
    "555-123-4567",
    "5551234567",
    "(555) 123-4567",
    "555.123.4567"
]
for phone in test_phones:
    result = format_phone_number(phone)
    print(f"{phone} → {result}")
print()


# ==========================================
# PRACTICE 12: Find Words with Specific Pattern
# ==========================================

def find_words_pattern(text, pattern):
    """
    Find all words matching a regex pattern.
    """
    return re.findall(pattern, text)


# Test Practice 12
print("=== PRACTICE 12: Find Words with Pattern ===")
text12 = "hello world python programming java javascript"

# Find words starting with 'p'
result_p = find_words_pattern(text12, r'\bp\w+')
print(f"Words starting with 'p': {result_p}")

# Find words ending with 'n'
result_n = find_words_pattern(text12, r'\w+n\b')
print(f"Words ending with 'n': {result_n}")

# Find words with 5 letters
result_5 = find_words_pattern(text12, r'\b\w{5}\b')
print(f"Words with exactly 5 letters: {result_5}")
print()


# ==========================================
# PRACTICE 13: Extract and Format Dates
# ==========================================

def extract_dates(text):
    """
    Extract dates in format DD-MM-YYYY or DD/MM/YYYY
    """
    pattern = r'\d{2}[-/]\d{2}[-/]\d{4}'
    return re.findall(pattern, text)


# Test Practice 13
print("=== PRACTICE 13: Extract Dates ===")
text13 = "Meetings: 15-01-2024, 20/02/2024, 25-03-2024"
result13 = extract_dates(text13)
print(f"Text: {text13}")
print(f"Dates Found: {result13}")
print()


# ==========================================
# PRACTICE 14: Replace All Numbers with X
# ==========================================

def mask_numbers(text):
    """
    Replace all numbers with 'X'
    """
    return re.sub(r'\d', 'X', text)


# Test Practice 14
print("=== PRACTICE 14: Mask Numbers ===")
text14 = "My ID is 123456 and PIN is 7890"
result14 = mask_numbers(text14)
print(f"Original: {text14}")
print(f"Masked: {result14}")
print()


# ==========================================
# PRACTICE 15: Remove Special Characters
# ==========================================

def remove_special_chars(text):
    """
    Keep only letters, digits, and spaces.
    Remove all special characters.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


# Test Practice 15
print("=== PRACTICE 15: Remove Special Characters ===")
text15 = "Hello@World! This#Is$A%Test&2024."
result15 = remove_special_chars(text15)
print(f"Original: {text15}")
print(f"Cleaned: {result15}")
print()


print("="*60)
print("ALL PRACTICES COMPLETE!")
print("="*60)