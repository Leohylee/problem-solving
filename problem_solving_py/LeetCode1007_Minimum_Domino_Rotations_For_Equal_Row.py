# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        mp = {}
        cnt = {}
        for i in range(0, len(tops)):
            if tops[i] != bottoms[i]:
                mp[tops[i]] = mp.get(tops[i], "") + "+"
                mp[bottoms[i]] = mp.get(bottoms[i], "") + "-"
                cnt[tops[i]] = cnt.get(tops[i], 0) + 1
            cnt[bottoms[i]] = cnt.get(bottoms[i], 0) + 1
        max_num = max(cnt, key=cnt.get)
        if cnt[max_num] == len(tops):
            if mp.get(max_num) is None:
                return 0
            return min(mp[max_num].count("+"), mp[max_num].count("-"))
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDominoRotations([1,1], [1,1]))
