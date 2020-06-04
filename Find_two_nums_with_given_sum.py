"""
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""

def two_sum(list, k):
    nums = set()
    for el in list:
        if el in nums:
            return True
        nums.add(k - el)
    return False

if __name__ == "__main__":
    print(two_sum([4,7,1,-3,2], 5))
    # True