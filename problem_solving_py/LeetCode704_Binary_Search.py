# https://leetcode.com/problems/binary-search/

# Definition for singly-linked list.
from cmath import pi
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            else:
                if nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))
