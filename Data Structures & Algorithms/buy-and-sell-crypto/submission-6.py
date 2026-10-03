class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        n = len(prices)
        profit = 0
        for i in range(n):
            profit = max(profit, prices[i]-buy)
            buy = min(buy, prices[i])
        
        return profit