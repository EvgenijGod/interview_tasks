"""
You are given an array. Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10,
 so the return value should be 5 (profit = 10 - 5 = 5).
"""


def buy_and_sell(arr):  # O(2n)
    i = len(arr) - 1
    max_elem = arr[i]
    while i >= 0:
        if arr[i] > max_elem:
            max_elem = arr[i]
        arr[i] = max_elem - arr[i]
        i -= 1
    return max(arr)


if __name__ == "__main__":
    print(buy_and_sell([9, 11, 8, 5, 7, 10]))
    # 5
