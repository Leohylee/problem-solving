# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans += pow(26, len(columnTitle) - i - 1) * (ord(columnTitle[i]) - ord('A') + 1)
        return ans



if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("AA"))
