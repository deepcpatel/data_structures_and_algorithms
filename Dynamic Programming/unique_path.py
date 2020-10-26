# Link: https://leetcode.com/problems/unique-paths/

class Solution(object):
    def __init__(self):
        self.grid = None
        
    def path(self, x, y, m, n):
        if self.grid[y][x] == -1:
            count = 0
            if x+1<m:
                count += self.path(x+1, y, m, n)
            if y+1<n:
                count += self.path(x, y+1, m, n)
            self.grid[y][x] = count
        return self.grid[y][x]
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.grid = [[-1] * m for i in range(n)]
        self.grid[n-1][m-1] = 1
        return self.path(0, 0, m, n) 