"""
Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again).

def string_sculptor(text: str) -> str:
"""

def string_sculptor(text: str) -> str:
    new = ""
    count = 0

    for i in text:
        if i.isalpha():
            if count % 2 == 0:
                new += i.lower()
            else:
                new += i.upper()
            count += 1
        elif i == " ":
            count = 0
            new += i
        else:
            new += i
    return new