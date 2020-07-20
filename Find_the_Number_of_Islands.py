"""
Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.
"""


class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def destroy_island(self, grid, i, j):
        if not self.inRange(grid, i, j) or grid[i][j] != 1:
            return
        grid[i][j] = 0
        self.destroy_island(grid, i + 1, j)
        self.destroy_island(grid, i, j + 1)
        self.destroy_island(grid, i - 1, j)
        self.destroy_island(grid, i, j - 1)

    def numIslands(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 1
                    self.destroy_island(grid, i, j)
        return ans


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    print(Solution().numIslands(grid))
    # 3
