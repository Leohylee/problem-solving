# https://leetcode.com/problems/finding-3-digit-even-numbers/
#
# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.

from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        l = set()
        for i in range(len(digits)):
            s = digits[i] * 100
            if s == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                s1 = s + digits[j] * 10

                for k in range(len(digits)):
                    if j == k or i == k:
                        continue
                    if digits[k] % 2 != 0:
                        continue

                    s2 = s1 + digits[k]
                    if s2 % 2 == 0:
                        l.add(s2)

        return sorted(l)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findEvenNumbers([2,1,3,0]))
