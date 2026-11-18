"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.

Forbidden functions: sorted(), list.sort()

def cryptic_sorter(strings: list[str]) -> list[str]:
"""

def cryptic_sorter(strings: list[str]) -> list[str]:
    l = len(strings) - 1

    while l > 0:
        for i in range(0, l):
            if len(strings[i]) > len(strings[i + 1]):
                strings[i], strings[i + 1] = strings[i + 1], strings[i]
            elif len(strings[i]) == len(strings[i + 1]):
                if strings[i].lower() > strings[i + 1].lower():
                    strings[i], strings[i + 1] = strings[i + 1], strings[i]
        l -= 1
    return strings

print(cryptic_sorter(["ola", "la", "b", "a"]))