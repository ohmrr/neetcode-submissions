class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit, max_profit)

        # return max_profit

        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            
            sell += 1
        
        return max_profit