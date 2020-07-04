"""
You have a landscape, in which puddles can form. You are given an array of non-negative
integers representing the elevation at each location.
Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X
   X███XX█X
 X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
"""

from collections import deque


def capacity(arr):  # O(3N)
    right_border = []
    left_border = []
    i = len(arr) - 1
    tmp = arr[i]
    while i >= 0:
        tmp = max(tmp, arr[i])
        right_border = [tmp] + right_border
        i -= 1
    tmp = arr[0]
    for el in arr:
        tmp = max(tmp, el)
        left_border.append(tmp)
    ans = 0
    for j in range(len(arr)):
        ans += min(left_border[j], right_border[j]) - arr[j]
    return ans


if __name__ == "__main__":
    print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # 6
    print(capacity([0, 1, 0]))
    # 0
    print(capacity([0, 4, 1, 3, 3]))
    # 2
