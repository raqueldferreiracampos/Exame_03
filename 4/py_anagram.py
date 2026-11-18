"""
Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.

def anagram(s1: str, s2: str) -> bool:
"""

def anagram(s1: str, s2: str) -> bool:
    new_s1 = ""
    new_s2 = ""
    for i in s1.lower():
        if i.isalpha():
            new_s1 += i
    for j in s2.lower():
        if i.isalpha():
            new_s2 += j
    return sorted(new_s2) == sorted(new_s1)