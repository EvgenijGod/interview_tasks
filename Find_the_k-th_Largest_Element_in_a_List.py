"""
Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
"""

import heapq

def findKthLargest(nums, k):  # O(N * log N )
    nums = sorted(nums)
    return nums[k]


def findKthLargest_better(nums, k): # O(N + (N - k) * log N)
    heapq.heapify(nums)
    n = len(nums)
    while n != k:
        n -= 1
        heapq.heappop(nums)
    return nums[0]


if __name__ == "__main__":
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
    # 5
    print(findKthLargest_better([3, 5, 2, 4, 6, 8], 3))
    # 5
