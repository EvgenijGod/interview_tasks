"""
You are given an array of integers. Return an array of the same size where the element at each
index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.
"""


def products(nums):  # O(N) time, O(N) memory
    tmp = 1
    forward = [1]
    backward = [1]
    for i in nums[:-1]:
        tmp *= i
        forward.append(tmp)
    tmp = 1
    for i in nums[::-1][:-1]:
        tmp *= i
        backward.append(tmp)
    ans = []
    n = len(nums)
    for i in range(n):
        ans.append(forward[i] * backward[n - 1 - i])
    return ans


if __name__ == "__main__":
    print(products([1, 2, 3, 4, 5]))
    # [120, 60, 40, 30, 24]
