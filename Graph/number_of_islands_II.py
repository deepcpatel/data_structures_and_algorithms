# Link: https://www.lintcode.com/problem/number-of-islands-ii/

# Approach: Every new land block can create three possibilities. If it is isolated (no neighbouring land), then it creates new island. If it has one surrounding island, then it can extend that island
# or else if there are detached surrounding island, then it joins them. Thus, we use union find algorithm to join the island. For that, we keep parent and number of children count of each island
# block. If two or more than two islands are to be merged, we merge smaller islands to the larger island. And at each iteration, we return the number of islands so far in our matrix.

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    
    def find(self, n):      # Find parent of current island
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, li):    # Join neighbouring islands
        max_c, sup_par, merged_island = float('-inf'), -1, 0
        
        for n in li:    # Finding the island with highest children (super island)
            parent = self.find(n)
            
            if self.nchildren[parent] > max_c:
                max_c = self.nchildren[parent]
                sup_par = parent
        
        for n in li:    # Merging other island with super island
            parent = self.find(n)
            
            if parent != sup_par:
                self.parents[parent] = sup_par
                self.nchildren[sup_par] += self.nchildren[parent]
                merged_island += 1
        
        return merged_island    # Returns number of merged islands. We will use it to decrement the total island count
        
    def find_neighbours(self, o, n, m):     # Finds surrounding lands if any
        li = []
        
        if o.x-1 >= 0 and self.land[o.x-1][o.y] != 0:
            li.append(self.land[o.x-1][o.y])
        
        if o.x+1 < n and self.land[o.x+1][o.y] != 0:
            li.append(self.land[o.x+1][o.y])
                
        if o.y-1 >= 0 and self.land[o.x][o.y-1] != 0:
            li.append(self.land[o.x][o.y-1])
                
        if o.y+1 < m and self.land[o.x][o.y+1] != 0:
            li.append(self.land[o.x][o.y+1])
                
        return li
    
    def numIslands2(self, n, m, operators):
        self.parents, self.nchildren, self.land, self.counter, num_island = {}, {}, [[0]*m for i in range(n)], 1, 0
        ans = []
        
        for o in operators:
            
            if self.land[o.x][o.y] == 0:    # Check if this cell already has land or not
                neighbours = self.find_neighbours(o, n, m)
                
                if len(neighbours) == 0:    # No surrounding land. Then create new one
                    npar, self.counter = self.counter, self.counter + 1
                    self.parents[npar], self.nchildren[npar] = npar, 0
                    num_island += 1
                else:                       # If current land block is joining surrounding island, then join those islands
                    merged_island = self.union(neighbours)
                    npar = self.find(neighbours[0])
                    num_island -= merged_island     # Decrementing total island count
                
                self.land[o.x][o.y] = npar 
                self.nchildren[npar] += 1   # Update children of parent island
                
            ans.append(num_island)  # Append total number of islands
            
        return ans