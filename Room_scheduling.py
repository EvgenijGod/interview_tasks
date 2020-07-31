"""
You are given an array of tuples (start, end) representing time intervals for lectures.
The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""

import heapq as hq


def room_amnt(arr):  # O(N * log N)
    rooms = []
    num = 0
    arr = sorted(arr)
    for begin, end in arr:
        if rooms == []:
            hq.heappush(rooms, end)
        else:
            tmp = None
            while rooms:
                tmp = hq.heappop(rooms)
                if tmp >= begin:
                    break
                tmp = None
            if tmp is not None:
                hq.heappush(rooms, tmp)
            hq.heappush(rooms, end)
        num = max(num, len(rooms))
    return num


if __name__ == "__main__":
    print(room_amnt([(30, 75), (0, 50), (60, 150)]))
    # 2 1.5 2 3.0 2 2.0 2
