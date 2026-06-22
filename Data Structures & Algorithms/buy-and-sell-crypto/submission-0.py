class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy_day = 0
        max_profit = 0

        for sell_day in range(len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, profit)

            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
        
        return max_profit
