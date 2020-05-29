"""
Given a sorted array, A, with possibly duplicated elements,
find the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.
"""


class Solution:
    def getRange(self, arr, target):
        got_num = False
        left = right = -1
        for index, i in enumerate(arr):
            if i > target:
                break
            if i == target:
                if got_num is False:
                    got_num = True
                    left = right = index
                else:
                    right += 1
        return left, right

if __name__ == "__main__":
    # Test program
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]
