# Link: https://leetcode.com/problems/longest-valid-parentheses/

class Solution(object):
    def __init__(self):
        self.ar = None
        self.str_size = 0
        self.s = None
        
    def matcher(self):
        sum_count = 0
        stack = []
        
        for i in range(self.str_size):
            if sum_count == 0 and self.s[i] == ')':
                continue
            elif sum_count > 0 and self.s[i] == ')':
                ix = stack.pop()
                sum_count -= 1
                self.ar[ix] = 1
                self.ar[i] = 1
            else:
                stack.append(i)
                sum_count += 1
                
    def longestValidParentheses(self, s):
        self.s = s
        self.str_size = len(self.s)
        self.ar = [0]*self.str_size
        self.matcher()
        
        max_sum = 0
        sumi = 0
        for i in range(self.str_size):
            
            if sumi + self.ar[i]>sumi:
                sumi += 1
            else:
                if sumi>max_sum:
                    max_sum = sumi
                sumi = 0
        
        if sumi>max_sum:
            max_sum = sumi
        return max_sum 
