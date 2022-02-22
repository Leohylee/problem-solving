# https://leetcode.com/problems/majority-element/
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        return max(hm, key=hm.get)


if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3]))
