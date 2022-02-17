# https://leetcode.com/problems/4sum-ii/
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0

        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1

        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
