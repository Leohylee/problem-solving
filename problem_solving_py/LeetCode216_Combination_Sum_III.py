# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.backtrack([], [], 1, k, n)

    def backtrack(self, temp: List[int], ans: List[List[int]], start: int, limit: int, target: int):
        if sum(temp) == target and len(temp) == limit:
            ans.append(list(temp))
            return
        elif sum(temp) > target or len(temp) >= limit:
            return
        for num in range(start, 10):
            temp.append(num)
            self.backtrack(temp, ans, num + 1, limit, target)
            temp.pop()
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum3(3,9))
