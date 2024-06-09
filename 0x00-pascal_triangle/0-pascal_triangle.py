#!/usr/bin/python3
"""
    pascals triangle
    finding the solution had me pulling my hair out
"""


def pascal_triangle(n):
    """ The function returns pascals triangle columns """

    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1]

        if row_num > 0:
            for i in range(1, row_num):
                numb = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
                row.append(numb)
            row.append(1)

        triangle.append(row)

    return triangle
