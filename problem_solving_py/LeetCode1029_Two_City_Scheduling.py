# https://leetcode.com/problems/two-city-scheduling/

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = {}
        totalCost = 0
        a = b = len(costs) / 2
        for idx, cost in enumerate(costs):
            difference[idx] = max(cost) - min(cost)
        while difference:
            candidate = max(difference, key=difference.get)
            if a > 0 and b > 0:
                city = costs[candidate].index(min(costs[candidate]))
                totalCost = totalCost + costs[candidate][city]
                if city == 0:
                    a = a - 1
                else:
                    b = b - 1
            elif a > 0:
                totalCost = totalCost + costs[candidate][0]
                a = a - 1
            elif b > 0:
                totalCost = totalCost + costs[candidate][1]
                b = b - 1
            difference.pop(candidate)
        return totalCost



if __name__ == "__main__":
    solution = Solution()
    print(solution.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
