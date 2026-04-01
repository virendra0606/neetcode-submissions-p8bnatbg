class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]
        for i in range(1,len(prices)):
            current_profit = prices[i]-price
            if profit<current_profit:
                profit = current_profit
            price = min(prices[i],price)
        return profit
            
        