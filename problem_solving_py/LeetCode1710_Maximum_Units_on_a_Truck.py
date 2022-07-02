# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=1)
        n, i, ans = len(boxTypes), 0, 0
        while i < n and truckSize > 0:
            ans += min(truckSize, boxTypes[i][0]) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))
