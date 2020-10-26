# Link: https://leetcode.com/problems/clone-graph/

# Approach: Basically iterate the given node using BFS and create its neighbours simultaneously. Moreover, store them in some list so that we can retrieve them when needed (here cloned_graph).

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return None
        
        cloned_graph, queue = [None]*100, deque([node])
        cloned_graph[node.val-1] = Node(node.val, None)
        
        while queue:    # BFS
            node1 = queue.popleft()

            if node1.neighbors:     # If neighbour exists then make a list to store them, otherwise leave it None
                if not cloned_graph[node1.val-1].neighbors:
                    cloned_graph[node1.val-1].neighbors = []

                for nbr in node1.neighbors:                 # Iterating over neighbours
                    if cloned_graph[nbr.val-1] == None:     # If neighbour node does not exist in list, then make a new one and append it for BFS exploration
                        cloned_graph[nbr.val-1] = Node(nbr.val, None)
                        queue.append(nbr)
                    
                    cloned_graph[node1.val-1].neighbors.append(cloned_graph[nbr.val-1]) # Store neighbours into neighbour list of the new graph
                        
        return cloned_graph[node.val-1]