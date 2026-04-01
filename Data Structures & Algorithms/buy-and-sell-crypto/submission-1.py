class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]: #if sell is less than buy, check max_profit
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: #if sell is MORE than buy, move left pointer to right pointer
                l = r
            r += 1 #always move right pointer over
        return max_profit



