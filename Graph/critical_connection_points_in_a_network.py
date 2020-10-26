# Link: https://leetcode.com/problems/critical-connections-in-a-network/
# Reference: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

# Tarjan's Algorithm
# Finding Articulation Points

class Solution(object):
    
    def get_critical_node(self, node):
        self.low[node] = self.time
        self.disc[node] = self.time
        self.visited[node] = True
        self.time += 1
        children = 0
        
        for n in self.graph[node]:
            if self.visited[n] == False:
                self.parent[n] = node
                self.get_critical_node(n)
                
                children += 1
                
                self.low[node] = min(self.low[node], self.low[n])
                
                if self.parent[node] == -1 and children > 1:
                    self.ap[node] = True
                    
                if self.parent[node] != -1 and self.low[n] >= self.disc[node]:
                    self.ap[node] = True
            
            elif n != self.parent[node]:
                self.low[node] = min(self.low[node], self.disc[n])
                
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.graph = {}
        self.ap = [False]*n         # Articulate Point
        self.visited = [False]*n
        self.parent = [-1]*n
        self.disc = [-1]*n
        self.low = [-1]*n
        self.time = 0
        self.ans = []
        
        for c in connections:
            if c[0] not in self.graph:
                self.graph[c[0]] = [c[1]]
            else:
                self.graph[c[0]].append(c[1])
                
            if c[1] not in self.graph:
                self.graph[c[1]] = [c[0]]
            else:
                self.graph[c[1]].append(c[0])
                
        self.get_critical_node(0)
        
        for i in range(n):
            if self.ap[i] == True:
                self.ans.append(i)

        return self.ans 
