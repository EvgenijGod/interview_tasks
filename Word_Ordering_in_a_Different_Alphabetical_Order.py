"""
Given a list of words, and an arbitrary alphabetical order, verify that the words
are in order of the alphabetical order.

Example:
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
Explanation: The words are in increasing alphabetical order
"""


def isSorted(words, order_):
    n = len(words)
    if n == 1:
        return True
    order = dict()
    for i, el in enumerate(order_):
        order[el] = i
    i = 1
    while i < n:
        len_2 = len(words[i])
        len_1 = len(words[i - 1])
        min_len = min(len_1, len_2)
        j = 0
        res = 0 # i-1 vs i
        while j < min_len:
            i2 = order[words[i][j]]
            i1 = order[words[i - 1][j]]
            if i1 < i2:
                res = 1
                break
            if i1 > i2:
                res = -1
                break
            j += 1
        if res == -1 or len_1 > len_2:
            return False
        i += 1
    return True


if __name__ == "__main__":
    print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
    # False
    print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
    # True
