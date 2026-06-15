class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0

        for currentPrice in prices:
            minPrice = min(currentPrice, minPrice)
            currentProfit = currentPrice - minPrice
            maxProfit = max(currentProfit, maxProfit)

        return maxProfit