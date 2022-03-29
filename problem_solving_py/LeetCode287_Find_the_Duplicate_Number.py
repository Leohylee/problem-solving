# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break

        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate([1,3,4,2,2]))
