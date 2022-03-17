# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        s = s.replace("()", "1")
        score, s = self.sub(s)
        return score

    def sub(self, s):
        score = 0
        while len(s) > 0:
            if s[0] == "1":
                score = score + 1
                s = s[1:]
            elif s[0] == "(":
                subTotal, s = self.sub(s[1:])
                score = subTotal + score
            elif s[0] == ")":
                return score * 2, s[1:]
        return score, s

if __name__ == "__main__":
    solution = Solution()
    print(solution.scoreOfParentheses("()(()(()))(())()"))
