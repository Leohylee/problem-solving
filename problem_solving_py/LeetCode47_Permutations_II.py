# https://leetcode.com/problems/permutations-ii/
from typing import List, Set


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(list(num) for num in self.backtrack([], set(), list(nums), len(nums)))

    def backtrack(self, temp: List[int], ans: Set[tuple], pool: List[int], size: int):
        if len(temp) == size:
            ans.add(tuple(temp))
            return
        for i in range(len(pool)):
            temp.append(pool.pop(0))
            self.backtrack(temp, ans, pool, size)
            pool.append(temp.pop())
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))
