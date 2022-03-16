# https://leetcode.com/problems/validate-stack-sequences/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        curr = []
        cnt = -1
        while pushed or popped:
            pop = popped[0]
            if len(curr) > 0 and curr[-1] == pop:
                popped.pop(0)
                curr.pop(-1)
            elif pushed:
                curr.append(pushed.pop(0))
            if not pushed:
                if cnt == len(popped):
                    return False
                else:
                    cnt = len(popped)
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
