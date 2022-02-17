# https://leetcode.com/problems/subarray-sum-equals-k/
#
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        d = dict()
        d[0] = 1
        cnt = 0
        for num in nums:
            sum += num
            cnt += d.get((sum - k), 0)
            d[sum] = d.get(sum, 0) + 1
        return cnt


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 2, 3], 3))
