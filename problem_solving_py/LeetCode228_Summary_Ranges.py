# https://leetcode.com/problems/summary-ranges/

from typing import List


class Solution:
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))
