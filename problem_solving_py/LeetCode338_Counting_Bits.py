# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = []
        for i in range(0, n + 1):
            binRep = "{0:b}".format(i)
            cnt.append(binRep.count('1'))
        return cnt



if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(5))
