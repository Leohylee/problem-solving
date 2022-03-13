# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        q = []
        for i in range(0, len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                q.append(s[i])
            else:
                if len(q) == 0:
                    return False
                else:
                    cur = q.pop(-1)
                    if cur == "{" and s[i] != "}" or cur == "[" and s[i] != "]" or cur == "(" and s[i] != ")":
                        return False
        return len(q) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("(()"))
