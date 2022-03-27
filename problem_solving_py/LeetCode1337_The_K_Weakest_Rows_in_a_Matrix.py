# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = sorted(range(m), key=lambda i: (mat[i], i))
        del rows[k:]
        return rows


if __name__ == "__main__":
    solution = Solution()
    print(solution.kWeakestRows([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3))
