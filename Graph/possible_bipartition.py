# Link: https://leetcode.com/problems/possible-bipartition/

# Approach: Construct the graph out of given edges. We then create a set known as 'visited' which stores which set does a node belong (either 0 or 1) and it is initialized with -1. Now we iterate
# over all graph nodes and if its set is not determined, we do BFS over it. We explore each neighbouring node 'n' of our current node 'node'. If 'n' is belonging to same set as 'node', then it signifies
# that there is an edge 'e' which connects two nodes in same set (line 30). This means that the graph is not Bipartite. Else, we assign opposite set of 'node' to 'n' and move on (line 27). In short: 
# Adjacent points cannot be in same set.

from collections import deque

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph, queue, visited = [[] for i in range(N)], deque(), [-1]*N
        
        for e in dislikes:
            a, b = e[0]-1, e[1]-1
            graph[a].append(b)
            graph[b].append(a)
            
        for i in range(N):
            if visited[i] == -1:
                queue.append(i)
                
                while queue:
                    node = queue.popleft()
                    
                    if visited[node] == -1:
                        visited[node] = 0
                        
                    for n in graph[node]:                        
                        if visited[n] == -1:
                            queue.append(n)
                            visited[n] = 1 - visited[node]
                        elif visited[n] == visited[node]:
                            return False
        return True