# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#
# Given an array nums of integers, return how many of them contain an even number of digits.

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.findNumbers([12,345,2,6,7896]))
