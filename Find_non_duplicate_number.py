"""
Given a list of numbers, where every number shows up twice except for one number,
find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory.
"""

def singleNumber(nums):
    ans = 0
    for i in nums:
        ans ^= i
    return ans


if __name__ == "__main__":
    print(singleNumber([4, 3, 2, 8283, 4, 1, 3, 2, 1, 8284, 8283]))
    # 8284

