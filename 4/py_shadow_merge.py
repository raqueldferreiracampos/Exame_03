"""
Write a function that merges two sorted lists into one sorted list.

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
"""

def merge_harvest_rows(list1: list[int], list2: list[int]) -> list[int]:
    new = []
    for i in list1:
        new.append(i)
    for j in list2:
        new.append(j)
    l = len(new) - 1
    while l > 0:
        for k in range(l):
            if new[k] > new[k + 1]:
                new[k], new[k + 1] = new[k + 1], new[k]
        l -= 1
    return new