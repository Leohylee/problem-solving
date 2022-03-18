# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_oc = {n: i for i, n in enumerate(s)}
        ans = ""
        curr = -1
        while len(last_oc) > 0:
            idx = last_oc[min(last_oc, key=last_oc.get)]
            small = ""
            for i in range(curr + 1, idx + 1):
                if s[i] not in ans and (small == "" or ord(s[i]) < ord(small)):
                    small = s[i]
                    curr = i
            ans = ans + small
            last_oc.pop(small)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicateLetters("efdcbfdcabfd"))
