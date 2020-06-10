"""
Given a list of numbers, find if there exists a pythagorean triplet in that list.
A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
"""


def findPythagoreanTriplets(nums): #O(n^2)
    n = len(nums)
    hash = set()
    for i in range(n):
        if nums[i] ** 2 in hash:
            return True
        for j in range(i + 1, n):
            hash.add(nums[j] ** 2 + nums[i] ** 2)
    return False

def findPythagoreanTriplets_second(nums): #O(max*max)
    maximum = max(nums)
    hash_map = [0] * (maximum + 1)
    for num in nums:
        hash_map[num] = 1

    for i in range(maximum + 1):
        if hash_map[i] == 0:
            continue
        for j in range(1, maximum + 1):
            if hash_map[j] == 0 or (i == j and hash_map[i] == 1):
                continue
            val = int((i ** 2 + j ** 2) ** 0.5)
            if val ** 2 != i ** 2 + j ** 2:
                continue
            if val > maximum:
                continue
            if hash_map[val]:
                return True
    return False


if __name__ == "__main__":
    print(findPythagoreanTriplets([3, 12, 1, 13]))
    # True
