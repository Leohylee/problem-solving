# https://leetcode.com/problems/valid-parentheses/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        dial = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        pool = []
        for digit in digits:
            pool.append(dial[digit])
        return self.backtrack("", [], pool)

    def backtrack(self, temp: str, ans: List[str], pool: List[List[str]]):
        if len(pool) == 0:
            ans.append(temp)
            return ans
        curr = pool.pop(0)
        for alp in curr:
            temp = temp + alp
            ans = self.backtrack(temp, ans, list(pool))
            temp = temp[:len(temp)-1]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("2432423"))
