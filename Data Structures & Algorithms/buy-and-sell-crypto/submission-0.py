class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, maximum, profit = prices[0],0,0

        for i in prices:
            if i < minimum:
                minimum = i
                maximum = 0
            if i > maximum:
                maximum = i

            profit = max(profit, maximum-minimum)

        return profit