# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach: Store the maximum and minimum at each state of array. And calculate difference till that and store max 
# difference. If you update minimum number, then re inirialize max number as next max number should be only after 
# minimum number.


class Solution(object):
    def maxProfit(self, prices):
        maxn, minn, max_diff = float('-inf'), float('inf'), float('-inf')
        
        if len(prices)<2:
            return 0
        
        for i in range(len(prices)):
            if maxn<prices[i]:
                maxn = prices[i]
                
            if minn>prices[i]:
                minn = prices[i]
                maxn = minn
                
            if max_diff<maxn-minn:
                max_diff = maxn-minn
        
        return max_diff