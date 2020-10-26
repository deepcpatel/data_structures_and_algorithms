# Link: https://leetcode.com/problems/coin-change/

'''
# Approach: (Not my solution)
For the iterative solution, we think in bottom-up manner. Before calculating F(i)F(i)F(i), we have to compute all minimum counts for amounts up to iii. On each iteration iii of the algorithm F(i)F(i)F(i) is computed as min⁡j=0…n−1F(i−cj)+1\min_{j=0 \ldots n-1}{F(i -c_j)} + 1minj=0…n−1​F(i−cj​)+1

Bottom-up approach using a table to build up the solution to F6.

In the example above you can see that:

F(3)=min⁡{F(3−c1),F(3−c2),F(3−c3)}+1=min⁡{F(3−1),F(3−2),F(3−3)}+1=min⁡{F(2),F(1),F(0)}+1=min⁡{1,1,0}+1=1 \begin{aligned} F(3) &= \min\{{F(3- c_1), F(3-c_2), F(3-c_3)}\} + 1 \\ &= \min\{{F(3- 1), F(3-2), F(3-3)}\} + 1 \\ &= \min\{{F(2), F(1), F(0)}\} + 1 \\ &= \min\{{1, 1, 0}\} + 1 \\ &= 1 \end{aligned} F(3)​=min{F(3−c1​),F(3−c2​),F(3−c3​)}+1=min{F(3−1),F(3−2),F(3−3)}+1=min{F(2),F(1),F(0)}+1=min{1,1,0}+1=1​
'''

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        
        return (dp[amount] if dp[amount] != float('inf') else -1) 