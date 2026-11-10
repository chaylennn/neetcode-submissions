class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > best:
                best = profit
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1

        return best