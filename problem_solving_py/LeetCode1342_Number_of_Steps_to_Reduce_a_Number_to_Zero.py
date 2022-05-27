# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if not num: return 0
        res = 0
        while num:
            res += 1 + (num & 1)
            num >>= 1
        return res - 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSteps(14))
