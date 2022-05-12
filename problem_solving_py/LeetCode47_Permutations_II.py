# https://leetcode.com/problems/permutations-ii/
from collections import Counter
from typing import List, Set


class Solution:
    def permuteUnique(self, nums):
        def btrack(path, counter):
            if len(path)==len(nums):
                ans.append(path[:])
            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    btrack(path, counter)
                    path.pop()
                    counter[x] += 1
        ans = []
        btrack([], Counter(nums))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1,1,2]))
