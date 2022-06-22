# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for idx, num in enumerate(nums):
            if len(temp) > 0 and target - num in temp:
                return [temp[target - num], idx]
            temp[num] = idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([7,9,5,3,2,4], 9))
