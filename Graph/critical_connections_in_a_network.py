# Link: https://leetcode.com/problems/critical-connections-in-a-network/
# Reference: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

# Tarjan's Algorithm

class Solution(object):
    def get_critical_node(self, node):
        self.low[node] = self.time
        self.disc[node] = self.time
        self.time += 1
        
        for n in self.graph[node]:
            if n == self.parent[node]:
                continue
            
            if self.disc[n] == -1:
                self.parent[n] = node
                self.get_critical_node(n)
                    
                if self.low[n] > self.disc[node]:
                    self.ap[node] = True
                    self.ans.append([min(node, n), max(node, n)])
            
            self.low[node] = min(self.low[node], self.low[n])
                
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.graph = {}
        self.ap = [False]*n         # Articulate Point
        self.parent = [-1]*n
        self.disc = [-1]*n
        self.low = [-1]*n
        self.time = 0
        self.ans = []
        
        # Making  Graph
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
        return self.ans