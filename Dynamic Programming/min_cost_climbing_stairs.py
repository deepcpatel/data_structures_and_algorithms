# Link: https://leetcode.com/problems/min-cost-climbing-stairs/

# Approach: Start from second stair and find minimum cost of reaching there either from stair 0 or stair 1. Add that cost to current cost at second stair. Similarly, go to subsequent stair and find all
# all the cost. Finally return total minimum cost at second last stair or last stair.

class Solution(object):
    def minCostClimbingStairs(self, cost):
        N = len(cost)
        
        if N == 0:
            return 0
        elif N == 1:
            return cost[0]
        
        for i in range(2, N):
            cost[i] += min(cost[i-1], cost[i-2])
            
        return min(cost[N-1], cost[N-2]) 