"""
You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).
"""

from operator import itemgetter


def merge(intervals):  # O((N + 1) log(N))
    intervals = sorted(intervals, key=itemgetter(0))
    ans = []
    tmp = None
    for i in intervals:
        if tmp is None:
            tmp = i
        else:
            if tmp[1] < i[0]:
                ans.append(tmp)
                tmp = i
            else:
                tmp = (tmp[0], max(tmp[1], i[1]))
    if tmp is not None:
        ans.append(tmp)
    return ans


if __name__ == "__main__":
    print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
    # [(1, 3), (4, 10), (20, 25)]
