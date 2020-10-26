# Link: https://leetcode.com/problems/satisfiability-of-equality-equations/

# Approach: Union Find. Firts iterate all the equations having '==' operation. Union both the LHS and RHS symbol to connect to a common parent. Now, iterate through all the equations having '!='
# operator. For each LHS and RHS, find their paeremts using find() function. If both the parents are same then return False. Because '!=' signifies that LHS and RHS should not be connected and here
# they are. Return True at end if all things go well.

class Solution(object):
    def find(self, x):
        if self.char_par[x] != x:
            self.char_par[x] = self.find(self.char_par[x])
        return self.char_par[x]
    
    def union(self, a, b):            
        par_a = self.find(a)
        par_b = self.find(b)
        
        self.char_par[par_a] = par_b
        
    def equationsPossible(self, equations):
        a_num = ord('a')
        self.char_par = {chr(i+a_num):chr(i+a_num) for i in range(26)}
        
        for e in equations:
            if e[1] == '=':
                self.union(e[0], e[-1])
            
        for e in equations:
            if e[1] == '!':
                a_par, b_par = self.find(e[0]), self.find(e[-1])
                
                if a_par == b_par:
                    return False
                
        return True