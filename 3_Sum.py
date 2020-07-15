"""
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c)
in nums such that a + b + c = 0.
Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
"""


class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            x = nums[i]

            while left < right:
                if nums[left] + x + nums[right] == 0:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + x + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans


if __name__ == "__main__":
    nums = [1, -2, 1, 0, 5]
    print(Solution().threeSum(nums))
    # [[-2, 1, 1]]

    nums = [0, -1, 2, -3, 1]
    print(Solution().threeSum(nums))
    # [[-3, 1, 2], [-1, 0, 1]]