# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt = 1
        for ch in s:
            if len(stack) > 0 and stack[-1] == ch:
                cnt += 1
                stack.append(ch)
                if cnt == k:
                    for i in range(k):
                        stack.pop()
                    cnt = 1
                    i = 1
                    while len(stack) > i and stack[-i] == stack[-i-1]:
                        cnt += 1
                        i += 1
            else:
                cnt = 1
                stack.append(ch)
        return ''.join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("deeedbbcccbdaa", 3))
