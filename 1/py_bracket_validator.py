"""
Write a function that checks if the brackets in a string are valid.

A string is valid if every opening bracket has a matching closing bracket
in the correct order.

Allowed brackets: (), [], {}

def bracket_validator(s: str) -> bool:
"""

def bracket_validator(s: str) -> bool:
    stack = []
    dic = {"(": ")", "[": "]", "{": "}"}
    for i in s:
        if i in ("({["):
            stack.append(i)
        if stack and dic[stack[-1]] == i:
            stack.pop()
        elif not stack and i in dic.values():
            return False
    if not stack:
        return True
    else:
        return False
