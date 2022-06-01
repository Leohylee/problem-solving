# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for i, num in enumerate(nums):
            curr += num
            nums[i] = curr
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1,1,1,1,1]))