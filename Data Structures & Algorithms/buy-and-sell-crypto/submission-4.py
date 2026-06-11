class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        input prices as a list
        
        output is difference (lowest minus highest)
        
        hash for lowest?
        and hash for highest?
        
        two windows?
        
        
        hash where
        initial = -inf
        
        
        - loop through list compare with lowest, compare with highest
        - diff = lowest - highest
        diff = lowest - highest
        
        
        at 15 minute mark i give up look at solution
        
        i'th day.
        
        so im looking at the stock in order. 
        
        i have to check if i can buy or sell
        
        min_price vs max_price
        
        
        comfort level: low
        
        if not prices:
            return 0
        
        min_price = prices[0] # set min_price to first day's price.
        max_profit = 0 # zero if we already have a min_price. we will immediately calc max as soon as we hit first index.
        
        for price in prices[1:]: # offset by 1 because prices[0] is already set. so we can move to next day, and compare.
        
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
        
        
        ## brute force solution.
        
        def maxProfit(prices): 
            max_profit = 0     
            n = len(prices)
            
            for i in range(n):
                for j in range(i + 1, n): 
                    profit = prices[j] - prices[i]
                    if profit > max_profit:
                        max_profit = profit
            return max_profit

            
            
        ## brute force flow chart:
            flowchart TD
        A[prices: 7,1,5,3,6,4]
        
        B0[Buy Day 0: 7] -->|Sell| C1[Day 1: 1]
        B0 -->|Sell| C2[Day 2: 5]
        B0 -->|Sell| C3[Day 3: 3]
        B0 -->|Sell| C4[Day 4: 6]
        B0 -->|Sell| C5[Day 5: 4]
        
        B1[Buy Day 1: 1] -->|Sell| C2[Day 2: 5]
        B1 -->|Sell| C3[Day 3: 3]
        B1 -->|Sell| C4[Day 4: 6]
        B1 -->|Sell| C5[Day 5: 4]
        
        B2[Buy Day 2: 5] -->|Sell| C3[Day 3: 3]
        B2 -->|Sell| C4[Day 4: 6]
        B2 -->|Sell| C5[Day 5: 4]
        
        B3[Buy Day 3: 3] -->|Sell| C4[Day 4: 6]
        B3 -->|Sell| C5[Day 5: 4]
        
        B4[Buy Day 4: 6] -->|Sell| C5[Day 5: 4]
        
        B5[Buy Day 5: 4]
        
        sliding window checks condition for each index.
        """
        
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
        
        