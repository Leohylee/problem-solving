# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxValue = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxValue:
                maxValue = price - minPrice
        return maxValue


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
