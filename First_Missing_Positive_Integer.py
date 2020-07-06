"""
You are given an array of integers. Return the smallest positive integer that is not present in the array.
 The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest
positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.
"""


def first_missing_positive(nums):
    start = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
    if len(nums) == start:
        return 1

    for i in range(start, len(nums)):
        if abs(nums[i]) < len(nums) - start + 1 and nums[abs(nums[i]) - 1 + start] > 0:
            nums[abs(nums[i]) - 1 + start] *= -1

    for i in range(start, len(nums)):
        if nums[i] > 0:
            return i + 1 - start
    return len(nums) - start + 1


if __name__ == "__main__":
    print(first_missing_positive([3, 4, -1, 1]))
    # 2
