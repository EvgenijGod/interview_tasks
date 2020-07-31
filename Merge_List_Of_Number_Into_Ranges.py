"""
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']
Assume that all numbers will be greater than or equal to 0, and each element can repeat.
"""


def findRanges(nums):
    if not nums:
        return []
    ans = []
    begin = 0
    prev = begin
    for i in range(1, len(nums)):
        if nums[i] == prev + 1:
            prev += 1
        elif nums[i] > prev + 1:
            ans.append("{}->{}".format(nums[begin], nums[i - 1]))
            begin = i
            prev = nums[begin]
    ans.append("{}->{}".format(nums[begin], nums[len(nums) - 1]))
    return ans

if __name__ == "__main__":
    print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15, 19]))
    # ['0->2', '5->5', '7->11', '15->15', '19->19']
