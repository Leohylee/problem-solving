# https://leetcode.com/problems/add-two-numbers/
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = -100000000000
        for num in reversed(nums):
            if num < second:
                return True
            while len(stack) > 0 and stack[-1] < num:
                second = stack.pop()
            stack.append(num)
        return False



if __name__ == "__main__":
    solution = Solution()
    print(solution.find132pattern([3,6,4,1,2]))
