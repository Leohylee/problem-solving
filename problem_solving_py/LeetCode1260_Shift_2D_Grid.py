# https://leetcode.com/problems/shift-2d-grid/

from collections import defaultdict
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        gl, sl = len(grid), len(grid[0])
        q, mod = divmod(k, sl)
        if q >= gl:
            q = q % gl
        new = [[0] * sl for _ in range(gl)]
        for item in grid:
            for subitem in item:
                new[q][mod] = subitem
                if mod + 1 == sl:
                    mod = 0
                    if q + 1 == gl:
                        q = 0
                    else:
                        q = q + 1
                else:
                    mod = mod + 1
        return new

if __name__ == "__main__":
    solution = Solution()
    print(solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 100))
