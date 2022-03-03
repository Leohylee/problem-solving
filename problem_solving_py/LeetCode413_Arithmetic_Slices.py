# https://leetcode.com/problems/arithmetic-slices/
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = ans = 0
        if len(nums) < 3:
            return 0
        seq = nums[1] - nums[0]
        for i in range(0, len(nums)):
            if i < len(nums) - 1 and nums[i + 1] - nums[i] == seq:
                cnt = cnt + 1
            else:
                if cnt >= 2:
                    ans = ans + ((cnt - 1) / 2 * (1 + cnt - 1))
                cnt = 1
                if i < len(nums) - 1:
                    seq = nums[i + 1] - nums[i]
        return int(ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfArithmeticSlices([1,2,3,4,6,8,10,12,14]))
