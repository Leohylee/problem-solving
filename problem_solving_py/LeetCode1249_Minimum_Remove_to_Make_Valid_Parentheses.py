# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        open = []
        for i in range(0, len(s)):
            if s[i] == "(":
                open.append(len(ans))
            if s[i] == ")":
                if len(open) > 0:
                    open.pop(-1)
                else:
                    continue
            ans = ans + s[i]
        for idx, val in enumerate(open):
            ans = ans[0 : val - idx] + ans[val - idx + 1 :]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minRemoveToMakeValid("((((("))
