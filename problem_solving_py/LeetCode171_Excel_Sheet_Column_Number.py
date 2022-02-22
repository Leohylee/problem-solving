# https://leetcode.com/problems/subsets/
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans += pow(26, len(columnTitle) - i - 1) * (ord(columnTitle[i]) - ord('A') + 1)
        return ans



if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("AA"))
