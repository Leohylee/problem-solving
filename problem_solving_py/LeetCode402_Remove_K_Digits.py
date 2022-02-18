# https://leetcode.com/problems/remove-k-digits/
#
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer
# after removing k digits from num.


class Solution:
    def removeKdigits(self, num, k):
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeKdigits("34972309487263094827364097826349325003498623743450234823764", 10))
