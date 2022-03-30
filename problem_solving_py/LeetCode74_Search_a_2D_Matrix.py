# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, last = 0, len(matrix) - 1
        while last >= start:
            mp = (start + last) // 2
            if matrix[mp][0] <= target <= matrix[mp][-1]:
                return self.bs(matrix[mp], target)
            else:
                if target > matrix[mp][-1]:
                    start = mp + 1
                elif target < matrix[mp][0]:
                    last = mp - 1
        return False

    def bs(self, items, target):
        start, last = 0, len(items) - 1
        while last >= start:
            p = (start + last) // 2
            if items[p] == target:
                return True
            elif items[p] < target:
                start = p + 1
            elif items[p] > target:
                last = p - 1
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 13))
