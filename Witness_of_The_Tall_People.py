"""
There are n people lined up, and each have a height represented as an integer.
A murder has happened right in front of them, and only people who are taller than everyone
in front of them are able to see what has happened. How many witnesses are there?
"""


def witnesses(heights):
    witness_cnt = 0
    max_height = 0
    n = len(heights) - 1
    while n >= 0:
        if heights[n] > max_height:
            witness_cnt += 1
            max_height = heights[n]
        n -= 1
    return witness_cnt


if __name__ == "__main__":
    print(witnesses([3, 6, 3, 4, 1]))
    # 3


