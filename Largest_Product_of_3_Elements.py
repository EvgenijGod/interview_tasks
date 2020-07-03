"""
You are given an array of integers.
Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

"""

import heapq


def maximum_product_of_three(lst):  # O(N)
    heapq.heapify(lst)
    l1 = list(heapq.nsmallest(3, lst))
    l2 = list(heapq.nlargest(3, lst))
    print(l1, l2)
    return max(l1[0] * l1[1] * l1[2], l1[0] * l2[0] * l1[1], l2[0] * l2[1] * l2[2])


if __name__ == "__main__":
    print(maximum_product_of_three([-4, -42, 2, 8, 3, 5, 11, -4]))
    # 128
