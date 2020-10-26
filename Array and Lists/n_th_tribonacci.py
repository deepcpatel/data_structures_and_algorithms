# Link: https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def __init__(self):
        self.dict = {}
        self.dict[0] = 0
        self.dict[1] = 1
        self.dict[2] = 1
        
    def tribonacci(self, n: int) -> int:
        sum = 0
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.sum_tri(n)
    
    def sum_tri(self, n):
        
        n1 = 0
        n2 = 0
        n3 = 0
        
        if n-1 in self.dict:
            n1 = self.dict[n-1]
        else:
            n1 = self.sum_tri(n-1)
            self.dict[n-1] = n1
            
        if n-2 in self.dict:
            n2 = self.dict[n-2]
        else:
            n2 = self.sum_tri(n-2)
            self.dict[n-2] = n2
            
        if n-3 in self.dict:
            n3 = self.dict[n-3]
        else:
            n3 = self.sum_tri(n-3)
            self.dict[n-3] = n3
        return n1+n2+n3 
