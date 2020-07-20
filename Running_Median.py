"""
You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

"""


def get_position(arr, num):  # O(log N)
    if arr == []:
        return 0
    left = 0
    right = len(arr) - 1

    while right - left > 1:
        curr = (left + right) // 2
        if arr[curr] >= num:
            right = curr
        else:
            left = curr
    if num < arr[left]:
        return left
    if num > arr[right]:
        return right + 1
    return right


def running_median(stream):  # less then O(N * log N)
    sort_arr = []
    ans = []
    for num in stream:
        sort_arr.insert(get_position(sort_arr, num), num)
        n = len(sort_arr)
        if n % 2 == 1:
            ans.append(sort_arr[n // 2])
        else:
            ans.append((sort_arr[n // 2] + sort_arr[n // 2 - 1]) / 2)
    return ans


if __name__ == "__main__":
    print(running_median([2, 1, 4, 7, 2, 0, 5]))
    # 2 1.5 2 3.0 2 2.0 2
