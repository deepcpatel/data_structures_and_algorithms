# Link: https://leetcode.com/problems/climbing-stairs/

# Approach: The number of ways to reach current step depends on sum of number of ways to reach previous two steps.

class Solution(object):
    def climbStairs(self, n):
        ar = [0]*n
        
        if n == 0:
            return 0
        elif n == 1:
            ar[0] = 1
        else:
            ar[0], ar[1] = 1, 1
        
        for i in range(1, n):
            if i-1 >= 0:
                ar[i] += ar[i-1]
            
            if i-2 >= 0:
                ar[i] += ar[i-2]
                
        return ar[-1]

'''
# Other Solution
class Solution(object):
    def climbStairs(self, n):
        ar = [0]*n
        
        if n == 0:
            return 0
        elif n == 1:
            ar[0] = 1
        else:
            ar[0], ar[1] = 1, 2
        
        for i in range(2, n):
            ar[i] += ar[i-1] + ar[i-2]
                
        return ar[-1]
'''