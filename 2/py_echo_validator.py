"""
Write a function that checks if a string is a palindrome,
ignoring spaces and case, only consider alphabetic characters
for the comparison.

def echo_validator(text: str) -> bool:
"""

def echo_validator(text: str) -> bool:
    new = ""
    for i in text:
        if i.isalpha():
            new += i
    if not new:
        return False
    if new == new[::-1]:
        return True

print(echo_validator(" x2x  "))