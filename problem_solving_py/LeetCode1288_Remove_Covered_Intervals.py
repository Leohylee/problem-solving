# https://leetcode.com/problems/remove-covered-intervals/
#
# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that
# are covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.

from collections import defaultdict
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = right = 0
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        for i, j in intervals:
            ans += j > right
            right = max(right, j)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
