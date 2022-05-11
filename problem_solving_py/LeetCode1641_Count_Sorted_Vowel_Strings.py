# https://leetcode.com/problems/count-sorted-vowel-strings/
from typing import List


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [1,1,1,1,1]
        for j in range(1, n):
            for i in range(len(vowels)):
                vowels[i] = sum(vowels[i:len(vowels)])
        return sum(vowels)



if __name__ == "__main__":
    solution = Solution()
    print(solution.countVowelStrings(50))
