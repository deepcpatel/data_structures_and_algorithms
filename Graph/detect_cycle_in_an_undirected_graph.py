# Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1/

# Approach: Apply DFS on unvisited node (0). Keep track of visited node (-1) and nodes already in DFS loop (1). During DFS, if you encounter a node (1), then it is cycle. Return True for that. Also,
# One thing to keep in mind for undirected graph is that, nodes are two ways A->B and B->A. Thus, if you visit B from A using DFS, then during DFS on B, you don't visit back to A, because it will false
# count it as cycle, thus you keep track of parent node and do not visit it back.

def dfs(node, visited, graph, parent):
    for n in graph[node]:
        if n != parent:
            if visited[n] == 0:
                visited[n] = 1
                
                if dfs(n, visited, graph, node):
                    return True
            elif visited[n] == 1:
                return True
        
    visited[node] = -1
    return False

def isCyclic(g,n):
    visited = [0]*n # Keeps list of visited nad unvisited nodes
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            if dfs(i, visited, g, None):
                return 1

    return 0
