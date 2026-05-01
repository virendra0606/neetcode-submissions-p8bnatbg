class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cp = prices[0]
        for price in range(1,len(prices)):
            max_profit = prices[price]-cp
            profit = max(profit,max_profit)
            cp = min(cp,prices[price])
        return profit
        