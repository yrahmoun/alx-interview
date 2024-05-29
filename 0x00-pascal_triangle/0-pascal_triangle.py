#!/usr/bin/python3
"""returns a pascal triangle"""


def pascal_triangle(n):
    """returns a list of integers as a pascal triangle"""

    triangle = []
    if n <= 0:
        return traingle
    for row_num in range(n):
        if row_num == 0:
            row = [1]
        else:
            previous_row = [0] + triangle[row_num - 1] + [0]
            row = [previous_row[i] + previous_row[i + 1]
                   for i in range(len(previous_row) - 1)]
        triangle.append(row)
    return triangle
