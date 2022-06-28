# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, used, ans = collections.Counter(s), [], 0
        for c, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                ans += 1
            used.append(freq)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDeletions("aaabbbcccee"))
