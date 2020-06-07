"""
You are given a positive integer N which represents the number of steps in a staircase.
You can either climb 1 or 2 steps at a time.
Write a function that returns the number of unique ways to climb the stairs.

"""


def staircase(n): # O(n) memory and time
    arr = [0] * n
    if n <= 2:
        return 1
    arr[0] = 1
    arr[1] = 2
    i = 2
    while i < n:
        arr[i] = arr[i - 1] + arr[i - 2]
        i += 1
    return arr[n - 1]


if __name__ == "__main__":
    print(staircase(4))
    # 5
    print(staircase(5))
    # 8
