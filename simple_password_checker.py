"""
simple_password_checker.py
--------------------------
A simple password security tool that:
✔ Analyzes password strength
✔ Checks against common passwords
✔ Provides suggestions for improvement
✔ Generates random strong passwords
✔ Displays security best practices

Author: Shaik Abdul Jabbar 
License: MIT
"""

import random
import string
from common_passwords import COMMON_PASSWORDS, COMMON_PASSWORDS_SET


def count_characters(password):
    """Count different types of characters in the password."""
    uppercase = lowercase = digits = special = 0
    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    return uppercase, lowercase, digits, special


def is_common_password(password):
    """Check if password is in the common password database."""
    return password.lower() in COMMON_PASSWORDS_SET


def calculate_password_score(password):
    """Calculate password strength score (0-10)."""
    score = 0
    length = len(password)
    uppercase, lowercase, digits, special = count_characters(password)

    # Length scoring
    if length >= 20:
        score += 5
    elif length >= 16:
        score += 4
    elif length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1

    # Character variety scoring
    if uppercase > 0: score += min(uppercase, 2)
    if lowercase > 0: score += min(lowercase, 2)
    if digits > 0: score += min(digits, 2)
    if special > 0: score += min(special, 2)

    # Bonus for very long passwords
    if length >= 25:
        score += 1

    return min(score, 10)


def get_password_strength(password):
    """Determine password strength level."""
    if not password:
        return "None"
    if is_common_password(password):
        return "Very Weak"
    score = calculate_password_score(password)
    if score >= 8:
        return "Strong"
    elif score >= 5:
        return "Medium"
    else:
        return "Weak"


def get_password_suggestions(password):
    """Suggest improvements for a given password."""
    suggestions = []
    uppercase, lowercase, digits, special = count_characters(password)

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if len(password) < 12:
        suggestions.append("Consider using 12+ characters for better security")
    if uppercase == 0:
        suggestions.append("Add uppercase letters (A-Z)")
    if lowercase == 0:
        suggestions.append("Add lowercase letters (a-z)")
    if digits == 0:
        suggestions.append("Add numbers (0-9)")
    if special == 0:
        suggestions.append("Add special characters (!@#$%^&*)")
    if is_common_password(password):
        suggestions.append("CRITICAL: This password is commonly used and unsafe!")

    # Encourage more variety
    unique_chars = len(set(password.lower()))
    if unique_chars < len(password) * 0.6:
        suggestions.append("Use more unique characters")

    return suggestions


def analyze_password(password):
    """Print a detailed analysis of the password."""
    print("\n" + "="*50)
    print("PASSWORD ANALYSIS RESULTS")
    print("="*50)

    if not password:
        print("No password provided!")
        return

    strength = get_password_strength(password)
    score = calculate_password_score(password)
    uppercase, lowercase, digits, special = count_characters(password)

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Length: {len(password)} characters")
    print(f"Strength: {strength}")
    print(f"Score: {score}/10")

    print(f"\nCharacter Breakdown:")
    print(f"- Uppercase letters: {uppercase}")
    print(f"- Lowercase letters: {lowercase}")
    print(f"- Numbers: {digits}")
    print(f"- Special characters: {special}")
    print(f"- Unique characters: {len(set(password))}")

    print(f"\nSecurity Check:")
    if is_common_password(password):
        print("❌ DANGER: This password is in the common passwords list!")
    else:
        print("✅ Password not found in common passwords database")

    suggestions = get_password_suggestions(password)
    if suggestions:
        print("\nSuggestions for Improvement:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
    else:
        print("\n✅ No suggestions - password looks strong!")


def generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a random strong password."""
    if length < 4: length = 4
    if length > 50: length = 50

    chars = string.ascii_lowercase
    if use_uppercase: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_special: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    return ''.join(random.choice(chars) for _ in range(length))


def show_common_passwords():
    """Show top 10 common passwords to avoid."""
    print("\n" + "="*40)
    print("COMMON PASSWORDS TO AVOID")
    print("="*40)
    for i, pwd in enumerate(COMMON_PASSWORDS[:10], 1):
        print(f"{i:2d}. {pwd}")
    print(f"\nTotal in database: {len(COMMON_PASSWORDS)} passwords")


def show_security_tips():
    """Display best practices for password security."""
    tips = [
        "Use unique passwords for each account",
        "Use at least 12 characters",
        "Include uppercase, lowercase, numbers, and symbols",
        "Avoid personal information",
        "Don't use dictionary words",
        "Use a password manager",
        "Enable two-factor authentication",
        "Update passwords regularly",
        "Never share your passwords",
        "Check for data breaches regularly",
    ]
    print("\n" + "="*40)
    print("PASSWORD SECURITY TIPS")
    print("="*40)
    for i, tip in enumerate(tips, 1):
        print(f"{i:2d}. {tip}")


def main():
    """Main program menu."""
    print("="*50)
    print("SIMPLE PASSWORD SECURITY TOOL")
    print("="*50)

    while True:
        print("\n1. Analyze a password")
        print("2. Generate a password")
        print("3. Generate multiple passwords")
        print("4. View common passwords")
        print("5. Security tips")
        print("6. Exit")
        print("-"*50)

        choice = input("Choose an option (1-6): ").strip()
        if not choice.isdigit() or int(choice) not in range(1, 7):
            print("Invalid input. Please enter 1-6.")
            continue

        choice = int(choice)
        if choice == 1:
            password = input("\nEnter password to analyze: ")
            analyze_password(password)
        elif choice == 2:
            length = int(input("Length (4-50, default 16): ") or 16)
            password = generate_password(length)
            print(f"\nGenerated password: {password}")
            analyze_password(password)
        elif choice == 3:
            length = int(input("Length (4-50, default 16): ") or 16)
            print(f"\n5 Generated Passwords ({length} chars each):")
            print("-" * 40)
            for i in range(5):
                pwd = generate_password(length)
                strength = get_password_strength(pwd)
                score = calculate_password_score(pwd)
                print(f"{i+1}. {pwd} - {strength} ({score}/10)")
        elif choice == 4:
            show_common_passwords()
        elif choice == 5:
            show_security_tips()
        elif choice == 6:
            print("\nGoodbye! Stay secure!")
            break

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
