# https://leetcode.com/problems/delete-and-earn/

import collections


class Solution(object):
    def deleteAndEarn(self, nums):
        points, prev, curr = collections.Counter(nums), 0, 0
        for value in range(10001):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr


if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteAndEarn([2, 2, 3, 3, 3, 4, 5, 5]))
