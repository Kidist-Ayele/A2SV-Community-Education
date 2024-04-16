from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []
        for row in range(n-2):
            res = []
            for col in range(n-2):
                mat = [grid[r][c] for r in range(row, row+3) for c in range(col, col+3)]
                maximum = max(mat)
                res.append(maximum)
            result.append(res)
        return result    