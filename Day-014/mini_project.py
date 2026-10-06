"""
Day 14 - Mini Project
Project: Text File Analyzer

Topics Covered:
- File handling
- Reading files
- Writing files
- Appending files
- Context managers
- Word counting
- Word occurrence counting
- Text processing

Description:
Create a Text File Analyzer that allows the user to enter
text, saves it to a file, analyzes the file, and saves
the word frequency results into another file.
"""

import string


# ============================================================
# FUNCTION 1: SAVE TEXT TO FILE
# ============================================================

def save_text(text):
    """Save the user's text into input.txt."""

    with open("input.txt", "w") as file:
        file.write(text)


# ============================================================
# FUNCTION 2: READ TEXT FROM FILE
# ============================================================

def read_text():
    """Read and return the contents of input.txt."""

    with open("input.txt", "r") as file:
        return file.read()


# ============================================================
# FUNCTION 3: COUNT WORDS
# ============================================================

def count_words(text):
    """Return the total number of words."""

    words = text.split()

    return len(words)


# ============================================================
# FUNCTION 4: COUNT CHARACTERS
# ============================================================

def count_characters(text):
    """Return the total number of characters."""

    return len(text)


# ============================================================
# FUNCTION 5: COUNT LINES
# ============================================================

def count_lines(text):
    """Return the total number of lines."""

    return len(text.splitlines())


# ============================================================
# FUNCTION 6: WORD FREQUENCY
# ============================================================

def word_frequency(text):
    """Return a dictionary containing word frequencies."""

    words = text.lower().split()

    frequency = {}

    for word in words:

        # Remove punctuation
        word = word.strip(string.punctuation)

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


# ============================================================
# FUNCTION 7: FIND MOST FREQUENT WORD
# ============================================================

def most_frequent_word(frequency):
    """Return the most frequently occurring word."""

    if not frequency:
        return None

    return max(frequency, key=frequency.get)


# ============================================================
# FUNCTION 8: SAVE WORD FREQUENCY
# ============================================================

def save_word_frequency(frequency):
    """Save word frequency into word_count.txt."""

    with open("word_count.txt", "w") as file:

        for word, count in frequency.items():
            file.write(f"{word}: {count}\n")


# ============================================================
# FUNCTION 9: DISPLAY RESULTS
# ============================================================

def display_results(text, frequency):
    """Display all text analysis results."""

    total_words = count_words(text)
    total_characters = count_characters(text)
    total_lines = count_lines(text)

    frequent_word = most_frequent_word(frequency)

    print("\n" + "=" * 50)
    print("              TEXT FILE ANALYZER")
    print("=" * 50)

    print(f"Total Words      : {total_words}")
    print(f"Total Characters : {total_characters}")
    print(f"Total Lines      : {total_lines}")

    print("\nWord Frequency")
    print("-" * 50)

    for word, count in frequency.items():
        print(f"{word:<20}: {count}")

    if frequent_word:
        print("\nMost Frequent Word")
        print("-" * 50)
        print(
            f"{frequent_word} "
            f"({frequency[frequent_word]} times)"
        )

    print("=" * 50)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 50)
    print("          DAY 14 - TEXT FILE ANALYZER")
    print("=" * 50)

    print("\nEnter your text below.")
    print("You can enter a sentence or multiple lines.")
    print("Press Enter when finished.\n")

    text = input("Enter text: ")

    # Check for empty input
    if not text.strip():
        print("\nNo text entered.")
        return

    # Step 1: Save text
    save_text(text)

    # Step 2: Read text from file
    text = read_text()

    # Step 3: Analyze text
    frequency = word_frequency(text)

    # Step 4: Display results
    display_results(text, frequency)

    # Step 5: Save word frequency
    save_word_frequency(frequency)

    print("\nFiles created:")
    print("1. input.txt")
    print("2. word_count.txt")

    print("\nText analysis completed successfully!")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()