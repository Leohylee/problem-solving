# https://leetcode.com/problems/single-number/
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_nums = defaultdict(int)
        for num in nums:
            dict_nums[num] += 1
            if dict_nums[num] > 1:
                dict_nums.pop(num)
        return list(dict_nums)[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([4, 1, 2, 1, 2]))
