# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stack = {}
        for num in nums:
            stack[num] = 1
        i, ans = 0, 0
        while i < len(nums):
            if nums[i] + 1 in stack or nums[i] - 1 in stack:
                ans = max(ans, self.unionFind(nums[i]-1, stack, -1) + 1 + self.unionFind(nums[i]+1, stack, 1))
            i += 1


    def unionFind(self, curr, stack: dict, dir):
        if stack[curr] is None:
            return 0
        return 1 + self.unionFind(stack[curr+dir], stack, dir)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
