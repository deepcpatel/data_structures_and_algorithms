# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Approach: Start iterating over array and find upward slopes (i.e, array[i-1] > array[i]). At every slope subtract max_element (at end) and min_element (at start)
# and add them to our profit.

class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        
        min_i, profit = prices[0], 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                profit += prices[i-1]-min_i
                min_i = prices[i]
                
        if prices[-1] > min_i:
            profit += prices[-1] - min_i
                
        return profit 