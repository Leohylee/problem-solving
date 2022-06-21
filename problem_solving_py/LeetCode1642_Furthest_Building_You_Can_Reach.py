# https://leetcode.com/problems/furthest-building-you-can-reach/
from typing import List
from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder = PriorityQueue()
        curr = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                ladder.put(diff)
                if ladder.qsize() > ladders:
                    bricks -= ladder.get()
            if bricks < 0:
                break
            curr = i
        return curr


if __name__ == "__main__":
    solution = Solution()
    print(solution.furthestBuilding([1, 2], 0, 0))
