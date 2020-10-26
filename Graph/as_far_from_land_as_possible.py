# Link: https://leetcode.com/problems/as-far-from-land-as-possible/

# Approach: First of all, we will add all the water bocks near land (coastal blocks) in the queue. Now, after that we will iterate each coastal block in the queue and identify their neighbours 
# that are not visited, and add them in the queue after incrementing their distance by one (line 45 and other similar lines). This way we will iterate all neighbouring water blocks using BFS and 
# identify the aximum distance.

from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        N, queue, cost_grid, max_score = len(grid), deque([]), [[-1]*len(grid) for i in range(len(grid))], -1
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:     # Adding all the water near land (coastal areas)
                    cost_grid[i][j] = 0
                    old_sz = len(queue)
                    
                    if i-1 >= 0 and cost_grid[i-1][j] == -1:
                        cost_grid[i-1][j] = cost_grid[i][j] + 1
                        queue.append((i-1, j))
                        
                    if j-1 >= 0 and cost_grid[i][j-1] == -1:
                        cost_grid[i][j-1] = cost_grid[i][j] + 1
                        queue.append((i, j-1))
                        
                    if i+1 < N and cost_grid[i+1][j] == -1:
                        cost_grid[i+1][j] = cost_grid[i][j] + 1
                        queue.append((i+1, j))
                        
                    if j+1 < N and cost_grid[i][j+1] == -1:
                        cost_grid[i][j+1] = cost_grid[i][j] + 1
                        queue.append((i, j+1))
                    
                    new_sz = len(queue)
            
                    if old_sz<new_sz: # Means atleast one element is added to queue
                        max_score = max(max_score, cost_grid[i][j] + 1)

        # BFS (Growing from coast to water and incrementing dostance of each farther water block)
        while queue:
            i, j = queue.popleft()
            old_sz = len(queue)
            
            if i-1 >= 0 and cost_grid[i-1][j] == -1:
                cost_grid[i-1][j] = cost_grid[i][j] + 1
                queue.append((i-1, j))

            if j-1 >= 0 and cost_grid[i][j-1] == -1:
                cost_grid[i][j-1] = cost_grid[i][j] + 1
                queue.append((i, j-1))

            if i+1 < N and cost_grid[i+1][j] == -1:
                cost_grid[i+1][j] = cost_grid[i][j] + 1
                queue.append((i+1, j))

            if j+1 < N and cost_grid[i][j+1] == -1:
                cost_grid[i][j+1] = cost_grid[i][j] + 1
                queue.append((i, j+1))
                
            new_sz = len(queue)
            
            if old_sz<new_sz: # Means atleast one element is added to queue
                max_score = max(max_score, cost_grid[i][j] + 1)
                
        return max_score if max_score>1 else -1 # If there is either no land or water then max_distance will be 1. In that case, return -1 