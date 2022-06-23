# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)
        for str in strs:
            while short != "" and short not in str[:len(short)]:
                short = short[:-1]
        return short


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["reflower","flow","flight","aaaaaaaaa"]))
