class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profits.append(prices[j] - prices[i])
        
        return max(profits)