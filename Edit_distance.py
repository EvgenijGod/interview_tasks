"""
Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution) needed to change one string to the other.
"""

import numpy as np


def distance(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    arr = np.zeros((n1 + 1) * (n2 + 1), dtype = int).reshape(n1 + 1, -1)
    for i in range(1, n1 + 1):
        arr[i][0] = i
    for i in range(1, n2 + 1):
        arr[0][i] = i
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            tmp = arr[i - 1][j - 1]
            if s1[i - 1] != s2[j - 1]:
                tmp += 1
            arr[i][j] = min(tmp, arr[i - 1][j] + 1, arr[i][j - 1] + 1)
    return arr[n1][n2]


if __name__ == "__main__":
    print(distance('biting', 'sitting'))
    # 2
    print(distance('arrogant', 'surrogate'))
    # 4