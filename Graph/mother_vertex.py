# Link: https://practice.geeksforgeeks.org/problems/mother-vertex/1/

'''
Approach:

What is a Mother Vertex? A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.

There can be more than one mother vertices in a graph. We need to output anyone of them. For example, in the below graph, vertices 0, 1 and 2 are mother vertices.
MotherVertex


We strongly recommend you to minimize your browser and try this yourself first.
How to find mother vertex?

    Case 1:- Undirected Connected Graph : In this case, all the vertices are mother vertices as we can reach to all the other nodes in the graph.
    Case 2:- Undirected/Directed Disconnected Graph : In this case, there is no mother vertices as we cannot reach to all the other nodes in the graph.
    Case 3:- Directed Connected Graph : In this case, we have to find a vertex -v in the graph such that we can reach to all the other nodes in the graph through a directed path.



A Naive approach : A trivial approach will be to perform a DFS/BFS on all the vertices and find whether we can reach all the vertices from that vertex. This approach takes O(V(E+V)) time, which is very inefficient for large graphs.

Can we do better? We can find a mother vertex in O(V+E) time. The idea is based on Kosaraju's Strongly Connected Component Algorithm. In a graph of strongly connected components, mother vertices are always vertices of source component in component graph. The idea is based on below fact.

If there exist mother vertex (or vertices), then one of the mother vertices is the last finished vertex in DFS. (Or a mother vertex has the maximum finish time in DFS traversal).

A vertex is said to be finished in DFS if a recursive call for its DFS is over, i.e., all descendants of the vertex have been visited.

How does the above idea work? Let the last finished vertex be v. Basically, we need to prove that there cannot be an edge from another vertex u to v if u is not another mother vertex (Or there cannot exist a non-mother vertex u such that u-→v is an edge). There can be two possibilities.

    Recursive DFS call is made for u before v. If an edge u-→v exists, then v must have finished before u because v is reachable through u and a vertex finishes after all its descendants.
    Recursive DFS call is made for v before u. In this case also, if an edge u-→v exists, then either v must finish before u (which contradicts our assumption that v is finished at the end) OR u should be reachable from v (which means u is another mother vertex).



Algorithm :

    Do DFS traversal of the given graph. While doing traversal keep track of last finished vertex 'v'. This step takes O(V+E) time.
    If there exist mother vertex (or vetices), then v must be one (or one of them). Check if v is a mother vertex by doing DFS/BFS from v. This step also takes O(V+E) time.
'''

def DFS(node, graph, visited):
    visited[node] = True
    
    for n in graph[node]:
        if not visited[n]:
            DFS(n, graph, visited)

def findMother(g, V):
    visited, last = [False]*V, -1
    
    # Finding Last Index
    for i in range(V):
        if not visited[i]:
            DFS(i, g, visited)
            last = i
    
    # Checking if we can reach all nodes from Last index
    visited = [False]*V
    DFS(last, g, visited)
    
    return (last if not any(i == False for i in visited) else -1) 
