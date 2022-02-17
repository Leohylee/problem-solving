# https://leetcode.com/problems/sequential-digits/
#
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digits = len(str(low))
        high_digits = len(str(high))
        ans = []
        for i in range(low_digits, high_digits + 1):
            ans += self.addSequential(i, low, high)
        return ans

    def addSequential(self, digits: int, low: int, high: int) -> List[int]:
        ans = []
        num_list = []
        for i in range(1, 10):
            if len(num_list) <= digits:
                num_list.append(i)
                if len(num_list) > digits:
                    num_list.pop(0)
                number = ''.join(str(x) for x in num_list)
                if (len(num_list) == digits) & (low <= int(number) <= high):
                    ans.append(number)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sequentialDigits(100, 300))
