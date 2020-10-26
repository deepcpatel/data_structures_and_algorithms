# Link: https://practice.geeksforgeeks.org/problems/find-whether-path-exist5238/1/

# Approach: Find the coordinate of 2 or 1 and do DFS on them to find path to 1 or 2 respectively. You can also use BFS to do this.

'''
from collections import deque

def BFS(source, M, N, dest):
    queue = deque([source])
    
    while queue:
        c = queue.popleft()
        
        if M[c[0]][c[1]] == dest:
            return True
        elif M[c[0]][c[1]] != 0:    # Important condition when doing BFS in matrix. If you miss, them same neighbour of two nodes will be added to queue and may create infinite loop. (Not essential in graph)
            M[c[0]][c[1]] = 0  # Visited
        
            if c[0]-1 >= 0 and M[c[0]-1][c[1]] != 0:
                queue.append((c[0]-1, c[1]))
            
            if c[1]-1 >= 0 and M[c[0]][c[1]-1] != 0:
                queue.append((c[0], c[1]-1))
            
            if c[0]+1 < N and M[c[0]+1][c[1]] != 0:
                queue.append((c[0]+1, c[1]))
                
            if c[1]+1 < N and M[c[0]][c[1]+1] != 0:
                queue.append((c[0], c[1]+1))
                
    return False
'''

def DFS(source, M, N, dest):
    x, y = source
    
    if M[x][y] == dest:
        return True
    else:
        M[x][y] = 0
        
        if x-1 >= 0 and M[x-1][y] != 0:
            ret = DFS((x-1, y), M, N, dest)
            
            if ret:
                return True
        
        if x+1 < N and M[x+1][y] != 0:
            ret = DFS((x+1, y), M, N, dest)
            
            if ret:
                return True
        
        if y-1 >= 0 and M[x][y-1] != 0:
            ret = DFS((x, y-1), M, N, dest)
            
            if ret:
                return True
        
        if y+1 < N and M[x][y+1] != 0:
            ret = DFS((x, y+1), M, N, dest)
            
            if ret:
                return True
        
        return False

def is_possible(M, N):
    '''
    M  : input matrix,  list of list
    N  : size of matrix
    '''
    
    for i in range(N):
        for j in range(N):
            if M[i][j] == 2:
                return int(DFS((i, j), M, N, 1))
            elif M[i][j] == 1:
                return int(DFS((i, j), M, N, 2)) 
