# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        count = 0
        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                count += 1
            elif nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations([1,1,1,1,1,1,1,1,1,1,3,-1], 2))
