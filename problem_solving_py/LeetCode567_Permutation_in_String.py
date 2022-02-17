# https://leetcode.com/problems/permutation-in-string/
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm, s1l, s2l = defaultdict(int), len(s1), len(s2)
        if s1l > s2l: return False
        for ch in s1:
            hm[ch] += 1
        for i in range(s1l - 1):
            if s2[i] in hm: hm[s2[i]] -= 1
        for j in range(-1, s2l - s1l + 1):
            if j > -1 and s2[j] in hm:
                hm[s2[j]] += 1
            if j+s1l < s2l and s2[j+s1l] in hm:
                hm[s2[j+s1l]] -= 1
            if all(val == 0 for val in hm.values()): return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
