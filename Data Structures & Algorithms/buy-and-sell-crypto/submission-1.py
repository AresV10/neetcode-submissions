class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, profit = prices[0],0
        for i in prices:
            if i < minimum:
                minimum = i
            profit = max(profit, i-minimum)
        return profit