"""
Day 13 - Mini Project
Text Analyzer

Topics:
- Regular Expressions (re module)
- String Formatting
- Word Count
- Palindrome Checker
"""

import re


def clean_text(text):
    """Remove unnecessary spaces and convert text to lowercase."""
    return text.strip().lower()


def extract_words(text):
    """Extract words using a regular expression."""
    return re.findall(r"\b\w+\b", text)


def count_words(text):
    """Count the number of words in the text."""
    words = extract_words(text)
    return len(words)


def check_palindrome(text):
    """
    Check whether the given text is a palindrome.

    Spaces, punctuation, and capitalization are ignored.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text.lower())

    return cleaned == cleaned[::-1]


def analyze_text(text):
    """Analyze the given text."""
    words = extract_words(text)

    return {
        "word_count": len(words),
        "character_count": len(text),
        "palindrome": check_palindrome(text)
    }


def display_results(text):
    """Display the text analysis results."""
    results = analyze_text(text)

    print("\n" + "=" * 45)
    print("             TEXT ANALYZER")
    print("=" * 45)

    print(f"{'Input Text':<20}: {text}")
    print(f"{'Word Count':<20}: {results['word_count']}")
    print(f"{'Character Count':<20}: {results['character_count']}")

    if results["palindrome"]:
        palindrome_result = "Yes"
    else:
        palindrome_result = "No"

    print(f"{'Palindrome':<20}: {palindrome_result}")

    print("=" * 45)


def main():
    print("=" * 45)
    print("        DAY 13 - TEXT ANALYZER")
    print("=" * 45)

    text = input("\nEnter a sentence or text: ")

    if not text.strip():
        print("Please enter some text.")
        return

    display_results(text)


if __name__ == "__main__":
    main()