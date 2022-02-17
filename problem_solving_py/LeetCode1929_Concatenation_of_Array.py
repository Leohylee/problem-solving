# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#
# Given an array nums of integers, return how many of them contain an even number of digits.

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums
        return nums + new_nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.getConcatenation([1,2,1]))
