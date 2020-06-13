"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.
"""


class Solution:  # o(n) time, 0(1) memory
    def minSubArrayLen(self, nums, s):
        left = 0
        right = 0
        sum = 0
        ans = len(nums) + 1
        while right < len(nums):
            sum += nums[right]
            while sum >= s:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        if ans == len(nums) + 1:
            return 0
        return ans


if __name__ == "__main__":
    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
    # 2

    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 100))
    # 0
