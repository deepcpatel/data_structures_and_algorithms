# Link: https://leetcode.com/problems/redundant-connection/

# Approach: For each edge, try to perform union of both nodes, if it is unsuccessful, then that edge is adding cycle to graph. The union operation performs union of nodes in the graph. If two 
# distinct nodes already have a same parent then there is a cycle in the graph (line 24), return unsuccesful union operation.

class Solution(object):
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Parent find operation with pruning
        return self.parent[x]
    
    def union(self, x, y):
        if x not in self.parent:    # If node is not present already, add it
            self.parent[x], self.size[x], xpar = x, 1, x
        else:
            xpar = self.find(x)     # Else find its parent
            
        if y not in self.parent:    # If node is not present already, add it
            self.parent[y], self.size[y], ypar = y, 1, y
        else:
            ypar = self.find(y)     # Else find its parent
        
        if (xpar == ypar) and (x != y):         # If two different nodes have same parent, then it is cyclic edge (return False)
            return False                        
        elif self.size[xpar]>self.size[ypar]:   # Merge with parent having large number of children
            self.parent[ypar] = xpar
            self.size[xpar] += self.size[ypar]
        else:
            self.parent[xpar] = ypar
            self.size[ypar] += self.size[xpar]
        return True
        
    def findRedundantConnection(self, edges):
        self.parent, self.size, ans_e = {}, {}, None
        
        for e in edges:
            if not self.union(e[0], e[1]):      # See if union is possible or not. Save the edge with unsuccessful union
                ans_e = e
        return ans_e