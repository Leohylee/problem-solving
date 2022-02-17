# https://leetcode.com/problems/k-diff-pairs-in-an-array/
#
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
#
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# Notice that |val| denotes the absolute value of val.

import collections
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = collections.Counter(nums)
        for num in cnt:
            if ((k > 0) & ((num - k) in cnt)) | ((k == 0) & (cnt[num] > 1)):
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findPairs([3,1,4,1,5], 2))
