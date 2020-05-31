"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
"""

def sortNums(arr):
    nums = dict()
    for i in arr:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1
    print(nums)
    keys_list = list(nums.keys())
    keys_list.sort()
    ans = []
    for key in keys_list:
        while nums[key] != 0:
            ans += [key]
            nums[key] -= 1
    return ans


if __name__ == "__main__":
    print(sortNums([3, 3, 2, 1, 3, 2, 1]))
    # [1, 1, 2, 2, 3, 3, 3]
