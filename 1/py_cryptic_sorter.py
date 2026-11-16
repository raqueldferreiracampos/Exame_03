"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and
lexically equal)
4. Equal strings will appear in the same order as in the input list.

Forbidden functions: sorted(), list.sort()

def cryptic_sorter(strings: list[str]) -> list[str]:
"""

def string_sort(strings: list[str]) -> list[str]:
    i = len(strings) - 1

    while i >= 0:
        for j in range(0, i):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
        i -= 1
    return strings


def ascii_sort(strings: list[str]) -> list[str]:
    i = len(strings) - 1

    while i > 0:
        for j in range(0, i):
            s1 = strings[j].lower()  #ola
            s2 = strings[j + 1].lower()  #adeus
            if len(s1) > len(s2):
                min_len = len(s2)
            else:
                min_len = len(s1)
            l = 0
            while l < min_len:
                if ord(s1[l]) > ord(s2[l]):
                    strings[j], strings[j + 1] = strings[j + 1], strings[j]
                l += 1
        i -= 1
    return strings


def cryptic_sorter(strings: list[str]) -> list[str]:
    sorted_list = string_sort(strings)
    ss_list = ascii_sort(sorted_list)
    return ss_list


teste = ["e", "d", "c", "b", "a"]
teste2 = string_sort(teste)
teste3 = ascii_sort(teste2)
print(teste3)
