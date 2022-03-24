# https://leetcode.com/problems/boats-to-save-people/

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        sorted_people = sorted(people)
        x, y = 0, len(sorted_people) - 1
        while y >= x:
            if sorted_people[x] + sorted_people[y] <= limit:
                x = x + 1
                y = y - 1
            else:
                y = y - 1
            ans = ans + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numRescueBoats([3,5,3,4], 5))
