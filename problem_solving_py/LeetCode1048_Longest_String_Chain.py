# https://leetcode.com/problems/longest-string-chain/
from collections import defaultdict
from typing import List


# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         def isPredecessor(word1, word2):
#             if len(word1) + 1 != len(word2): return False
#             i = 0
#             for c in word2:
#                 if i == len(word1): return True
#                 if word1[i] == c:
#                     i += 1
#             return i == len(word1)
#
#         words.sort(key=len)
#         n = len(words)
#         dp = [1] * n
#         ans = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if isPredecessor(words[j], words[i]) and dp[i] < dp[j] + 1:
#                     dp[i] = dp[j] + 1
#             ans = max(ans, dp[i])
#         return ans

# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         wordSet = set(words)
#
#         @lru_cache(None)
#         def dp(word):
#             ans = 1
#             for i in range(len(word)):
#                 predecessor = word[:i] + word[i + 1:]
#                 if predecessor in wordSet:
#                     ans = max(ans, dp(predecessor) + 1)
#             return ans
#
#         return max(dp(w) for w in words)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # sort words by its length
        ans = 0
        dp = defaultdict(int)
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp and dp[word] < dp[predecessor] + 1:
                    dp[word] = dp[predecessor] + 1
            ans = max(ans, dp[word])
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestStrChain(["a","ab","ac","bd","abc","abd","abdd"]))
