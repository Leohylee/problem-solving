# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        stack = {}
        for num in nums:
            stack[num] = 1
        i, ans = 0, 0
        while i < len(nums):
            if nums[i] in stack:
                ans = max(ans, self.unionFind(nums[i]-1, stack, -1) + 1 + self.unionFind(nums[i]+1, stack, 1))
            i += 1
        return ans


    def unionFind(self, curr, stack: dict, dir):
        if stack.get(curr) is None:
            return 0
        stack.pop(curr)
        return 1 + self.unionFind(curr + dir, stack, dir)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
