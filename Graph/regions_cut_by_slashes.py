# Link: https://leetcode.com/problems/regions-cut-by-slashes/

# Approach: Document: ./archive/regions_cut_by_slashes - Approach.pdf, Link: https://leetcode.com/problems/regions-cut-by-slashes/discuss/573875/JAVA-Union-Find-(explanation)
# Union Find. Divide each square cell into four triangles and try to merge them using Union and Find method

class Solution:
    def find(self, i):      # Finding Parent set
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]
    
    def union(self, x, y):  # Union of both parent sets into one
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return
        
        self.rootsN -= 1
        if self.root_size[rootx] >= self.root_size[rooty]:
            self.roots[rooty] = rootx
            self.root_size[rootx] += self.root_size[rooty]
        else:
            self.roots[rootx] = rooty
            self.root_size[rooty] += self.root_size[rootx]
    
    def root_calc(self, i, j, direc):
        return 4 * (self.N * i + j) + direc - 1
    
    def regionsBySlashes(self, grid):
        self.N, self.roots = len(grid), list(range(len(grid)**2*4))  # self.roots represents list of parent of each set number
        self.root_size = [1 for i in range(len(self.roots))]
        self.rootsN = len(self.roots)
        
        for i in range(self.N):
            for j in range(self.N):
                if j+1<self.N:
                    self.union(self.root_calc(i, j, 2), self.root_calc(i, j+1, 4))
                
                if i-1>=0:
                    self.union(self.root_calc(i, j, 1), self.root_calc(i-1, j, 3))
                    
                if grid[i][j] == '\\':
                    self.union(self.root_calc(i, j, 1), self.root_calc(i, j, 2))
                    self.union(self.root_calc(i, j, 3), self.root_calc(i, j, 4))
                    
                elif grid[i][j] == '/':
                    self.union(self.root_calc(i, j, 1), self.root_calc(i, j, 4))
                    self.union(self.root_calc(i, j, 2), self.root_calc(i, j, 3))
                
                else:
                    self.union(self.root_calc(i, j, 1), self.root_calc(i, j, 2))
                    self.union(self.root_calc(i, j, 4), self.root_calc(i, j, 1))       
                    self.union(self.root_calc(i, j, 3), self.root_calc(i, j, 4))
        
        return self.rootsN