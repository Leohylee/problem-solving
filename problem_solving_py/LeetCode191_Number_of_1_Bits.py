# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     return "{0:b}".format(n).count('1')

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(0b00011000000000000000000000001011))
