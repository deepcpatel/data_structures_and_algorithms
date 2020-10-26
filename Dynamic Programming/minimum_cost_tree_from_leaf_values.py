# Link: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

# Approach: Partition the Array and recursively find minimum cost of each subarray. Now, for current partition
# add min cost of left subtree and right tree along with product of max numbers from both subtree [as indicated 
# in question] and get min of current value with us and calculated value [Line 29]. Store all the computetion in
# an array so that we don't need to recalculate for each recursion. Moreover, also store max_values of each subtree as
# you progress so that we don't need to recalculate it either [Line 28].

class Solution(object):
    def  __init__(self):
        self.dict_p = []
        self.maxn = []
        self.arr = None
        
    def recur(self, i, j):
        if i == j:
            self.maxn[i][j] = self.arr[i]
            return 0
        
        if (j-i) == 1:
            self.maxn[i][j] = max(self.arr[i], self.arr[j])
            return self.arr[i]*self.arr[j] 
        
        if self.dict_p[i][j] == -1:   
            min_sum = float('inf')
        
            for k in range(i, j):
                self.maxn[i][j] = max(self.maxn[i][j], self.arr[k])
                min_sum = min(min_sum, (self.recur(i, k) + self.recur(k+1, j) + self.maxn[i][k]*self.maxn[k+1][j]))
                
            self.maxn[i][j] = max(self.maxn[i][j], self.arr[j])
            self.dict_p[i][j] = min_sum
        
        return self.dict_p[i][j]
    
    def mctFromLeafValues(self, arr):
        self.arr = arr
        for i in range(len(arr)):
            self.dict_p.append([-1]*len(arr))
            self.maxn.append([-1]*len(arr))
            
        return self.recur(0, len(arr)-1)