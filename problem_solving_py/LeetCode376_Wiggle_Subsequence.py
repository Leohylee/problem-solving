# https://leetcode.com/problems/first-missing-positive/

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        ans, up = 1, None
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and up is not False:
                ans += 1
                up = False
            elif nums[i-1] > nums[i] and up is not True:
                ans += 1
                up = True
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.wiggleMaxLength([1,17,8,6,7,4,9]))
