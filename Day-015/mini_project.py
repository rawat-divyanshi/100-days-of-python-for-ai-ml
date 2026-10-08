# ============================================================
# Day 15 - Mini Project
# Input Validator with Exception Handling
# ============================================================

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    return name.strip()


def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a valid integer.")

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    return age


def validate_email(email):
    if "@" not in email:
        raise ValueError("Email must contain '@'.")

    if email.strip() == "":
        raise ValueError("Email cannot be empty.")

    return email.strip()


def validate_marks(marks):
    try:
        marks = float(marks)
    except ValueError:
        raise ValueError("Marks must be a valid number.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    return marks


def input_validator():
    print("=" * 55)
    print("             DAY 15 - INPUT VALIDATOR")
    print("=" * 55)

    try:
        # Name
        name = input("Enter your name: ")
        name = validate_name(name)

        # Age
        age = input("Enter your age: ")
        age = validate_age(age)

        # Email
        email = input("Enter your email: ")
        email = validate_email(email)

        # Marks
        marks = input("Enter your marks: ")
        marks = validate_marks(marks)

    except ValueError as error:
        print("\nValidation Error:", error)

    else:
        print("\n" + "=" * 55)
        print("             VALIDATION SUCCESSFUL")
        print("=" * 55)

        print(f"{'Name':<15}: {name}")
        print(f"{'Age':<15}: {age}")
        print(f"{'Email':<15}: {email}")
        print(f"{'Marks':<15}: {marks}")

        print("=" * 55)
        print("All inputs are valid!")

    finally:
        print("\nValidation completed.")


def main():
    input_validator()


if __name__ == "__main__":
    main()

