# Link: https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1

# Approach: First explore all rotten oranges and put their co-ordinates into queue. Also, keep count of good oranges during that. Now, do BFS on all the rotten oranges and make fresh oranges rot during
# BFS. Do BFS by counting llevels and at each level end, increment the time. Do this until no rotten oranges is left in the queue. Also, simultaneously decrement fresh orange count as you make them rot.
# Finally if no fresh orange is left, then return the time, else return -1.

from collections import deque

def rotOranges(mat,r,c):
    rot_time, orange_counter, queue = -1, 0, deque()
    neighbor_idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                orange_counter += 1 # Counts Fresh Orange
            elif mat[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        qlen = len(queue)
        
        while qlen:
            cell = queue.popleft()
            
            for i, j in neighbor_idx:
                ni, nj = cell[0]+i, cell[1]+j
                
                if (0 <= ni < r) and (0 <= nj < c) and (mat[ni][nj] == 1):
                    orange_counter, mat[ni][nj] = orange_counter - 1, 2
                    queue.append((ni, nj))
            
            qlen -= 1
        
        rot_time += 1
    
    return (rot_time if not orange_counter else -1)