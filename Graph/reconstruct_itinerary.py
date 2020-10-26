# Link: https://leetcode.com/problems/reconstruct-itinerary/

# Approach: It is a simple DFS approach. First of all to construct the graph, use bisect.insort to add elements in sorted fashion. Now, start DFS from JFK and recursively continue till you encounter
# dead end (no further children to explore). At the end of DFS, append in the answer list (use deque for appending from left).

from bisect import insort
from collections import deque, defaultdict

class Solution(object):
    def dfs(self, node):
        for i in range(len(self.graph[node])):
            if self.graph[node][i] != -1:
                self.graph[node][i], temp = -1, self.graph[node][i] # Marking as visited
                self.dfs(temp)
                
        self.ans.appendleft(node)
                
    def findItinerary(self, tickets):
        self.graph, self.ans, self.n = defaultdict(list), deque(), len(tickets)+1
        
        for t in tickets:
            insort(self.graph[t[0]], t[1])  # Putting elements in sorted fashion
        
        self.dfs("JFK")
        return self.ans 