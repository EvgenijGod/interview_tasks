"""
Given a list of integers, return the bounds of the minimum range that
must be sorted so that the whole list would be sorted.
"""


def findRange(nums):
    left = [nums[-1]] * len(nums)
    right = [nums[0]] * len(nums)
    ind = 1
    while ind < len(nums):
        if right[ind - 1] < nums[ind]:
            right[ind] = nums[ind]
        else:
            right[ind] = right[ind - 1]
        ind += 1
    ind = len(nums) - 2
    while ind >= 0:
        if left[ind + 1] > nums[ind]:
            left[ind] = nums[ind]
        else:
            left[ind] = left[ind + 1]
        ind -= 1
    left_ind, right_ind = 0, len(nums) - 1
    left_num, right_num = nums[0] - 1, nums[-1] + 1
    while left_ind < len(nums) and nums[left_ind] >= left_num and nums[left_ind] <= left[left_ind]:
        left_ind += 1
        left_num = nums[left_ind]

    while right_ind >= 0 and nums[right_ind] >= right[right_ind] and nums[right_ind] <= right_num :
        right_ind -= 1
        right_num = nums[right_ind]
    if left_ind > right_ind:
        left_ind = right_ind = 1
    return left_ind, right_ind


if __name__ == "__main__":
    print(findRange([1, 7, 9, 5, 7, 8, 10]))
    # (1, 5)
