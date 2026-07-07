# Task 1: Language Translation Tool
# CodeAlpha AI Internship - June 2026

print("=== Hindi to English Translator ===")
hindi = input("Enter Hindi word: ")
words = {"namaste": "hello", "dhanyawad": "thank you", "paani": "water"}
print("English:", words.get(hindi.lower(), "Not found"))
