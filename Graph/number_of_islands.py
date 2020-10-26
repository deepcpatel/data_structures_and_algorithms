# Link: https://leetcode.com/problems/number-of-islands/

# Approach: Explore all the cells using for loops. Now at each cell when you encounter "1", append the island_counter and att that coordinates to the queue for BFS. Explore all 
# neighbouring land using BFS and mark each visited when adding to queue. Finally return island_counter.

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        
        if m == 0:
            return 0
        
        n, island_counter, queue = len(grid[0]), 0, deque()
        
        if n == 0:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_counter += 1
                    queue.append((i, j))
                    
                    # BFS
                    while queue:
                        y, x = queue.popleft()
                        
                        
                        if x-1 >= 0 and grid[y][x-1] == "1":
                            grid[y][x-1] = "-1"
                            queue.append((y, x-1))
                            
                        if x+1 < n and grid[y][x+1] == "1":
                            grid[y][x+1] = "-1"
                            queue.append((y, x+1))
                            
                        if y-1 >= 0 and grid[y-1][x] == "1":
                            grid[y-1][x] = "-1"
                            queue.append((y-1, x))
                        
                        if y+1 < m and grid[y+1][x] == "1":
                            grid[y+1][x] = "-1"
                            queue.append((y+1, x))
        return island_counter