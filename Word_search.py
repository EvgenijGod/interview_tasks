"""
Given this matrix, and the target word FOAM, you should return true,
as it can be found going up-to-down in the first column.
"""
import copy

def word_search(matrix, word):
    n = len(word) - 1
    arr = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                if word[0] == matrix[i][j]:
                    arr[i][j] = [0, 0]
                else:
                    arr[i][j] = [-1, -1]
            elif i == 0:
                tmp = arr[i][j - 1][1]
                arr[i][j] = [-1, -1]
                if word[tmp + 1] == matrix[i][j]:
                    arr[i][j][1] = tmp + 1
            else:
                arr[i][j] = [-1, -1]
                tmp = None
                if j == 0:
                    tmp = -1
                else:
                    tmp = arr[i][j - 1][1]
                if word[tmp + 1] == matrix[i][j]:
                    arr[i][j][1] = tmp + 1
                tmp = arr[i - 1][j][0]
                if word[tmp + 1] == matrix[i][j]:
                    arr[i][j][0] = tmp + 1
            if arr[i][j][1] == n or arr[i][j][0] == n:
                return True
    return False

if __name__ == "__main__":
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

    print(word_search(matrix, 'SS'))
    # True

    print(word_search(matrix, 'FOAM'))
    # True

    print(word_search(matrix, 'LOL'))
    # False
