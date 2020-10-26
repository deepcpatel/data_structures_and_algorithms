# Link: https://leetcode.com/problems/is-graph-bipartite/

# Approach: We first create a set known as 'nset' which stores which set does a node belong (either 0 or 1) and it is initialized with -1. Now we iterate over all graph nodes and if its set is not
# determined, we do BFS over it. We explore each neighbouring node 'k' of our current node 'n'. If 'k' is belonging to same set as 'n', then it signifies that there is an edge 'e' which connects two
# nodes in same set (line 30). This means that the graph is not Bipartite. Else, we assign opposite set of 'n' to 'k' and move on (line 27). In short: Adjacent points cannot be in same set

from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        nset, N, graph_Q = [-1 for i in range(len(graph))], len(graph), deque([])

        for i in range(N):
            if nset[i] == -1:
                graph_Q.append(i)
                
                # BFS
                while graph_Q:
                    n = graph_Q.popleft()
                    
                    # Determining home set Number of current node (either 0 or 1)
                    if nset[n] == -1:
                        nset[n] = 0 # Assigning default to 0
                    
                    # Exploring edges
                    for j in graph[n]:
                        if nset[j] == -1:        # If color of node is not determined
                            nset[j] = 1-nset[n]  # Setting to opposite set of home_set (0 if home_set == 1 else 1)
                            graph_Q.append(j)
                        elif nset[j] == nset[n]: # Checking whether opposite node is in same set n. True means edge is connecting nodes in same set
                                return False                                
        return True