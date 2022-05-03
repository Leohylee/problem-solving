# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start, end = -1, -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i] and start == -1:
                start = i
            elif nums[i] != sorted_nums[i] and start != -1:
                end = i
        return 0 if start == -1 or end == -1 else end - start + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([2]))
