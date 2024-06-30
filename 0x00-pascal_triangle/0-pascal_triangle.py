#!/usr/bin/python3
"""
Pascal's Triangle Module
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): The number of rows of Pascal's triangle to generate

    Returns:
        List[List[int]]: A list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):  # Update elements between the edges
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
