class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cp = prices[0]
        for i in range(1,len(prices)):
            max_profit = prices[i]-cp
            profit = max(profit,max_profit)
            cp = min(cp,prices[i])
        return profit
        