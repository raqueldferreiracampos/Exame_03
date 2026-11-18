"""
Given a 2D matrix (list of lists), return a new matrix where each row
is reversed.

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
"""
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[::-1])
    return new_matrix
