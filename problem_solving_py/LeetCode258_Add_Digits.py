# https://leetcode.com/problems/add-digits/
#
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> int:
        while not len(str(num)) == 1:
            num = self.sumDigits(num)
        return num

    def sumDigits(self, num: int) -> int:
        sum = 0
        for x in str(num):
            sum += int(x)
        return sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(38))
