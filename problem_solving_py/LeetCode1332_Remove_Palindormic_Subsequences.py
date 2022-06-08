# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        if s == s[::-1]: return 1
        return 2

if __name__ == "__main__":
    solution = Solution()
    print(solution.removePalindromeSub("babaaab"))
