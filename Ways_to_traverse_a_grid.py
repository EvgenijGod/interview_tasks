"""
You 2 integers n and m representing an n by m grid, determine the number of ways you can get
from the top-left to the bottom-right of the matrix y going only right or down.
"""

import math


def num_ways(n, m):
    return math.factorial(n + m - 2) // math.factorial(n - 1) // math.factorial(m - 1)


if __name__ == "__main__":
    print(num_ways(2, 2))
    # 2

    print(num_ways(1, 5))
    # 1

    print(num_ways(4, 5))
    # 1

