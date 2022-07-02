# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        h, w = 0, 0
        for i in range(len(horizontalCuts)-1):
            h = max(h, horizontalCuts[i+1] - horizontalCuts[i])
        for i in range(len(verticalCuts)-1):
            w = max(w, verticalCuts[i+1] - verticalCuts[i])
        return (h * w) % ((10 ** 9) + 7)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea(1000000000,1000000000,[2],[2]))
