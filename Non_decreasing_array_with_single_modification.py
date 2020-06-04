"""
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7]
should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1]
however, should return false, since there is no way to modify just one element to make the array non-decreasing.
"""


def check(nums):
    err = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if err is None:
                err = i
            else:
                return False
    if err is None or err == 0 or err == len(nums) - 2 or nums[err - 1] <= nums[err + 1] or nums[err] <= nums[err + 2]:
        return True
    return False

if __name__ == "__main__":
    print(check([13, 4, 7]))
    # True
    print(check([0, 1, 10000, 2, 5]))
    # True
    print(check([1, 2, 3, 1, 1, 0, -1, 1, 2, 3]))
    # False
