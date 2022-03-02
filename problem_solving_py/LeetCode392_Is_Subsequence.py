# https://leetcode.com/problems/is-subsequence/

from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = 0
        if len(s) == 0: return True
        for i in range(0, len(t)):
            if s[curr] == t[i]:
                curr = curr + 1
            if curr >= len(s): return True
        return curr == len(s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence("bh", "cahbcgdc"))
