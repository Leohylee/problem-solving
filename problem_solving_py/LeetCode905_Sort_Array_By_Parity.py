# https://leetcode.com/problems/sort-array-by-parity/
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] % 2 != 0:
                nums.append(nums.pop(i))
            else:
                i += 1
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([2,3,5,435,43,34,5,56,64,34,3,3,54,6,6546]))
