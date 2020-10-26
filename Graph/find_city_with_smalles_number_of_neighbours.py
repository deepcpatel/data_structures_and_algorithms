# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

# Approach: Apply Floyd-Warshall algorithm to find distance between each node in the graph. Now calculate number of nodes within given threshold distance for each node and return the one with smallest
# number of neigbours within distance.

class Solution(object):
    def floyd_warshall(self, distanceThreshold):
        N = len(self.node_dist)
        
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d_new, d_old = self.node_dist[i][k]+self.node_dist[k][j], self.node_dist[i][j]
                    
                    if d_new < self.node_dist[i][j]:
                        self.node_dist[i][j] = d_new
                        
                        # Incrementing number of neighbours within a distance threshold
                        if d_new <= distanceThreshold and d_old > distanceThreshold:
                            self.min_dist_nodes[i] += 1
    
    def findTheCity(self, n, edges, distanceThreshold):
        self.node_dist, self.min_dist_nodes = [[float('inf')]*n for i in range(n)], [0]*n   # Stores distance between nodes
        min_n, min_idx = float('inf'), -1
        
        for i in range(n):
            self.node_dist[i][i] = 0
        
        # Filling node distance
        for e in edges:
            i, j, dist = e[0], e[1], e[2]
            self.node_dist[i][j], self.node_dist[j][i] = dist, dist
            
            if dist <= distanceThreshold:
                self.min_dist_nodes[i] += 1
                self.min_dist_nodes[j] += 1
            
        self.floyd_warshall(distanceThreshold)
        
        # Finding the node with minimum neighbours
        for i in range(n):
            if self.min_dist_nodes[i] <= min_n:
                min_n = self.min_dist_nodes[i]
                min_idx = i
        
        return min_idx