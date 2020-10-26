# Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/

# Approach: This is shortest path and not shortest distance problem. Thus, BFS is ideal choice. Now start with 0 node of both the colors (add it i queue). Explore neighbours of them from alternate
# colored edges [add in the queue (node, distance, color) tuple, so that when exploreing neighbours, color' nodes will be explored]. During each exploration, compare distance woth respect to current
# distance. If new distance is smaller, then replace old one with the new one. Also keep list of visited nodes for both graphs to avoid cycling during visit.

from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        red_graph, blue_graph, queue, node_dist = [[] for i in range(n)], [[] for i in range(n)], deque(), [float('inf') for i in range(n)]
        visited = {'b':[-1 for i in range(n)], 'r':[-1 for i in range(n)]}  # Visited nodes list for both the colored graphs
        
        # Creating adjacency lists
        for re in red_edges:
            red_graph[re[0]].append(re[1])
            
        for be in blue_edges:
            blue_graph[be[0]].append(be[1])
            
        node_dist[0] = 0    # Starting point
            
        
        queue.append((0, 0, 'b'))   # Starting from exploring red edge. Input: (node, distance_from_0, colored_edge)
        queue.append((0, 0, 'r'))   # Starting from exploring blue edge
        
        while queue:
            node = queue.popleft()
            visited[node[2]][node[0]] = 1   # Marking particular node of a particular colored graph as visited
            
            if node[2] == 'b':
                for neighbour in red_graph[node[0]]:
                    node_dist[neighbour] = min(node[1]+1, node_dist[neighbour]) # Adding minimum distnace in the answer
                    if visited['r'][neighbour] == -1:   # If a node in red graph is not visited then add it for exploration
                        queue.append((neighbour, node[1]+1, 'r'))
            else:
                for neighbour in blue_graph[node[0]]:
                    node_dist[neighbour] = min(node[1]+1, node_dist[neighbour]) # Adding minimum distnace in the answer
                    if visited['b'][neighbour] == -1:   # If a node in blue graph is not visited then add it for exploration
                        queue.append((neighbour, node[1]+1, 'b'))
        
        return [-1 if x == float('inf') else x for x in node_dist] 