#!usr/bin/python3
"""
Create Pascal's triangle
"""


def pascal_triangle(n):
    """
    result- Full table of coefficients
    n- Number of rows of pascal's table
    i- Iterator for n
    coefficients- row of table
    prev- number directly above and to the left of the number
    curr- number above and to the right of it
    """
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        while (i <= n):
            coefficients = [1]
            if i == 1:
                break
            elif i == 2:
                coefficients.append(1)
                break
            else:
                while (len(coefficients) < len(result[-1])):
                    prev = result[-1][len(coefficients)-1]
                    curr = result[-1][len(coefficients)]
                    coefficients.append(prev+curr)
                else:
                    coefficients.append(1)
                    break
                i += 1
        result.append(coefficients)
    return result
