"""
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?
"""


class Solution:  # O(N)  time
    def sortColors(self, nums):
        zero_cnt = 0
        ptr = len(nums) - 1
        i = 0
        while i <= ptr:
            if nums[i] == 0:
                nums[i] = 1
                i += 1
                nums[zero_cnt] = 0
                zero_cnt += 1
            elif nums[i] == 2:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr -= 1
            else:
                i += 1

        return nums


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    print("Before Sort: ")
    print(nums)
    # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

    Solution().sortColors(nums)
    print("After Sort: ")
    print(nums)
    # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
