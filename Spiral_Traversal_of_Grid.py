"""
You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""


def matrix_spiral_print(M):
    right_border = len(M[0]) - 1
    left_border = 0
    up_border = 1
    down_border = len(M) - 1
    i, j = 0, 0
    mode = 0
    ans = []
    cnt = 0
    while True:
        if mode == 0:
            if j + 1 <= right_border:
                ans.append(M[i][j])
                j += 1
                cnt = 0
            else:
                mode = 1
                right_border -= 1
                cnt += 1
        elif mode == 1:
            if i + 1 <= down_border:
                ans.append(M[i][j])
                i += 1
                cnt = 0
            else:
                mode = 2
                down_border -= 1
                cnt += 1
        elif mode == 2:
            if j - 1 >= left_border:
                ans.append(M[i][j])
                j -= 1
                cnt = 0
            else:
                mode = 3
                left_border += 1
                cnt += 1
        elif mode == 3:
            if i - 1 >= up_border:
                ans.append(M[i][j])
                i -= 1
                cnt = 0
            else:
                mode = 0
                up_border += 1
                cnt += 1
        if cnt == 4:
            break
    print(ans)


if __name__ == "__main__":
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

    matrix_spiral_print(grid)
    # 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
