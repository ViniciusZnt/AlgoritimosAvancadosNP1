# Problema: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < buy_price:
                buy_price = i
            profit = max(profit, i - buy_price)

        return profit
