# Link: https://leetcode.com/problems/network-delay-time/

# Approach: Apply Djikstra's algorithm to find minimum time from start node K. Treat Time as Distance in the algorithm.

class Solution(object):
    
    def argmin(self, li):   # Function to find minimum node from the array
        minimum, min_idx = float('inf'), -1
        
        for i in range(len(li)):
            if self.visited[i] == 0 and minimum > li[i]:
                minimum, min_idx = li[i], i
                
        return min_idx
        
    def networkDelayTime(self, times, N, K):
        self.node_dict, self.dist, self.visited, self.count = {}, [float('inf') for i in range(N)], [0 for i in range(N)], N
        
        # Making Graph Data structure
        for t in times:
            if t[0] not in self.node_dict:
                self.node_dict[t[0]] = []
            self.node_dict[t[0]].append((t[1], t[2]))   # Appending destination and time
            
        self.dist[K-1] = 0    # Making K as starting node
        
        # Djikstra
        while self.count != 0:
            # Find minimum node
            min_node = self.argmin(self.dist)
            
            # Return 'Fail (-1)' if no minimum node is found
            if min_node == -1:
                return -1
            
            self.visited[min_node], self.count = -1, self.count-1   # Mark current node as visited
            
            # Explore neighbour of current minimum node and update their distance
            if min_node+1 in self.node_dict:
                for n in self.node_dict[min_node+1]:
                    alt = self.dist[min_node] + n[1]

                    if self.dist[n[0]-1] > alt:     # Update distance
                        self.dist[n[0]-1] = alt
                        
        return max(self.dist)