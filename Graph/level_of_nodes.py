# Link: https://practice.geeksforgeeks.org/problems/level-of-nodes1147/1/

# Approach: Do BFS starting from node 0. Also, at every level, count numbers of node in queue and if they are all popped out, increment the level. Also, while adding the node in the queue and while
# processing a node, ensure it is not visited. Finally, return a node if it equals to X.

from collections import deque

def levels(g, N, X):
    '''
    g[] : adjacency list of the given graph
    N : number of vertices
    X : The destination node
    '''
    
    queue, visited, level = deque([0]), [0]*N, 0
    
    if X >= N:  # X does not exist
        return -1
        
    while queue:
        lenq = len(queue)
        
        for i in range(lenq):
            node = queue.popleft()
            
            if node == X:
                return level
                    
            if not visited[node]:   # Checking whether current node is visited or not. When adding in queue, if neighbour node in same level exist, it may also be added without visited check
                visited[node] = 1
                
                for n in g[node]:
                    if not visited[n]:  # Not adding already cisited node. Neighbour Node in same level may escape this. That is why, we put extra check above
                        queue.append(n)
        
        level += 1
    
    return -1