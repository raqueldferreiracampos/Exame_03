"""
Write a function that checks if the brackets in a string are valid.

A string is valid if every opening bracket has a matching closing bracket
in the correct order.

Allowed brackets: (), [], {}

def bracket_validator(s: str) -> bool:
"""

def bracket_validator(s: str) -> bool:
    stack = []
    for i in s:
        if i in "([{":
            stack.append(i)
        elif i in ")}]":
            if not stack:
                return False
            if stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack[-1] == "{" and i == "}":
                stack.pop()
            elif stack[-1] == "[" and i == "]":
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False



def bracket_validator(s: str) -> bool:
    dic = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for i in s:
        if i in dic.keys():
            stack.append(i)
        if stack and dic[stack[-1]] == i:
            stack.pop()
        elif not stack and i in dic.values():
            return False
    return not stack

print(bracket_validator("()"))
