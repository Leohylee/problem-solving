# https://leetcode.com/problems/broken-calculator/

import math


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            half = target
            while half > startValue:
                half = half / 2
            while math.ceil(half) < startValue:
                startValue = startValue - 1
                ans = ans + 1
            startValue = startValue * 2
            ans = ans + 1
        if startValue > target:
            ans = ans + startValue - target
        return ans




if __name__ == "__main__":
    solution = Solution()
    print(solution.brokenCalc(2, 3))
