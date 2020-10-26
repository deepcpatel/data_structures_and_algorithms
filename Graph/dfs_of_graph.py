# Link: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1/

# Approach: Perform DFS of the graph. Make 'visited' list to keep track of visited node in order to avoid cycle.

'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''

def traverse(node, graph, visited, ans):
    if not visited[node]:
        ans.append(node)
        visited[node] = 1
        
        for n in graph[node]:
            traverse(n, graph, visited, ans)

def dfs(g,N):
    visited, ans = [0]*N, []
    
    for i in range(N):
        traverse(i, g, visited, ans)
    
    return ans