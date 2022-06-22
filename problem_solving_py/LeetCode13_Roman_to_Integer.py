# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        mapping = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s)):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
                ans -= mapping[s[i]]
            else:
                ans += mapping[s[i]]
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
