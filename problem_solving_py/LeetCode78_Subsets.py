# https://leetcode.com/problems/subsets/
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
