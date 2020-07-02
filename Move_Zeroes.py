"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeros_1(self, nums):  # O(n^2) time
        print(nums)
        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(1, i + 1):
                print(i, j)
                if nums[j - 1] == 0 and nums[j] != 0:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums

    def moveZeros(self, nums):  # O(n) time
        iter = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[iter] = nums[i]
                iter += 1
        for i in range(iter, n):
            nums[i] = 0
        return nums


if __name__ == "__main__":
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().moveZeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
