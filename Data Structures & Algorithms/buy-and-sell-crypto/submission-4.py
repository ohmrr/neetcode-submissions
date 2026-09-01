class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit, max_profit)

        # return max_profit

        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                right += 1
        
        return max_profit