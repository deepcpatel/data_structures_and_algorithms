# Link: https://leetcode.com/problems/divisor-game/

'''
# Approach: 
Whenever a number is even, there is always a way to win as you can produce an odd number to the next player by simply subtracting one.

However when you get an odd number N , there is no way to produce another odd number to your opponent by subtracting some divisor x as 
x will always be odd. So odd minus odd is even and the opponent will always win.
'''

class Solution(object):
    def divisorGame(self, N):
        if N % 2 == 0:
            return True
        else:
            return False 