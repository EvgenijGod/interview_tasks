"""
Given two arrays, write a function to compute their intersection -
the intersection means the numbers that are in both arrays.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""


class Solution:
    def intersection(self, nums1, nums2):
        a = dict()
        ans = []
        for i in nums1:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in nums2:
            if i in a:
                a[i] -= 1
                ans.append(i)
                if a[i] == 0:
                    a.pop(i)
        return ans


if __name__ == "__main__":
    print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    # [9, 4]
