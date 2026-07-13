# ==========================================================
# Day 006 - Mini Project
# Project: Number Guessing Game
# ==========================================================

print("=" * 55)
print("          WELCOME TO THE NUMBER GUESSING GAME")
print("=" * 55)

# Secret number
secret_number = 7

# Count the number of attempts
attempts = 0

while True:

    guess = int(input("\nEnter your guess (1-10): "))

    attempts += 1

    if guess == secret_number:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print(f"Total Attempts : {attempts}")
        break

    elif guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

print("\nThanks for playing!")
print("=" * 55)