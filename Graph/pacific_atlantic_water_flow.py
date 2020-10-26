# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

# Approach: Inherent algorithm is recursive DFS. First make two matrix atlantic and pacific to record the access to them from each point.
# Now start doing DFS from edges touching the oceans. For example for checking for Atlantic reachability to every point from matrix, we start doing DFS from bottom
# and Right edge of matrix and mark 1 if point is reachable. Similar method for finding Pacific reachability. Also, a point is reachable from ocean if no other point
# is blocking it (height of blocking point is greater than our point).

class Solution(object):
    def dfs(self, x, y, inp):
        inp[y][x] = 1
        
        for d in self.directions:
            c = x+d[0]
            r = y+d[1]
            
            if not (c<0 or c>=self.C or r<0 or r>=self.R or inp[r][c] or self.matrix[r][c]<self.matrix[y][x]):
                self.dfs(c, r, inp)
        
    def pacificAtlantic(self, matrix):
        if matrix == []:
            return []
        
        pacific = []
        atlantic = []
        self.matrix = matrix
        ans = []
        
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        self.R, self.C = len(self.matrix), len(self.matrix[0])
        
        pacific = [[0 for i in range (self.C)]for j in range (self.R)]
        atlantic = [[0 for i in range (self.C)]for j in range (self.R)]
        
        for i in range(self.C):
            self.dfs(i, 0, pacific)
            self.dfs(i, self.R-1, atlantic)
        
        for j in range(self.R):
            self.dfs(0, j, pacific)
            self.dfs(self.C-1, j, atlantic)
            
        for i in range(self.C):
            for j in range(self.R):
                if atlantic[j][i] and pacific[j][i]:
                    ans.append([j, i])  # Sending output (y, x) or (row, column) format
        return ans