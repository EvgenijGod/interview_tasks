"""
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.
"""


def max_subarray_sum1(arr):  # O(4n) time
    tmp_arr = []
    sum = 0
    for i in arr:
        sum += i
        tmp_arr.append(sum)
    it = len(arr) - 1
    max_num = tmp_arr[it]
    ans = max(tmp_arr)
    while it >= 0:
        max_num = max(max_num, tmp_arr[it])
        tmp_arr[it] = max_num - tmp_arr[it]
        it -= 1
    return max(max(tmp_arr), ans)


def max_subarray_sum(arr):  # O(N)
    result = 0
    cursum = 0
    for num in arr:
        cursum += num
        cursum = max(cursum, 0)
        result = max(result, cursum)
    return result


if __name__ == "__main__":
    print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
    # 137
    print(max_subarray_sum([-2, -5, 6, -2, -3, 1, 5, -6]))
    # 7
    print(max_subarray_sum([1, 2, 0, 3, 4, 5]))
    # 15
    print(max_subarray_sum([-1, 2, 0, -3, 4, -1, 5]))
    # 8
