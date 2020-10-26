# Link: https://www.lintcode.com/problem/paint-house/

# Approach: Start from second last house and calculate foe each house the sum of current value and minimum of alternate colouring of previous house as written in line 18, 19 and 20. Return the minimum 
# colouring of the first house.

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        N = len(costs)
        
        if N == 0:
            return 0
        
        for i in range(N-2, -1, -1):
            costs[i][0] += min(costs[i+1][1], costs[i+1][2])
            costs[i][1] += min(costs[i+1][0], costs[i+1][2])
            costs[i][2] += min(costs[i+1][0], costs[i+1][1])
        
        return min(costs[0])