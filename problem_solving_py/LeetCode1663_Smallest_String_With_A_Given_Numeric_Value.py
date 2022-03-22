# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n > k: return ""
        chrs = [1] * n
        k = k - n
        curr = 0
        while k > 0 and curr < len(chrs):
            if k > 25:
                chrs[curr] = chrs[curr] + 25
                k = k - 25
            else:
                chrs[curr] = chrs[curr] + k
                k = 0
            curr = curr + 1
            ans = ""
        for num in reversed(chrs):
            ans = ans + chr(96 + num)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSmallestString(20,100))
