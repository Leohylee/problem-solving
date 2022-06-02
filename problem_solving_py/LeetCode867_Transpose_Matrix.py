# https://leetcode.com/problems/transpose-matrix/
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(matrix) == 0: return []
        for i in range(len(matrix[0])):
            sub = []
            for j in range(len(matrix)):
                if len(matrix[j]) > i: sub.append(matrix[j][i])
            ans.append(sub)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.transpose([[1, 2, 3, 4], [4, 5, 6], [7, 8, 9]]))
