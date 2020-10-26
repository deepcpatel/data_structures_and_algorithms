# Link: https://leetcode.com/problems/maximal-square/

# Approach: At each grid location [i][j], if it is 0 then leave it because it does not form square, if its 1 then look at minimal squares in [i-1][j], [i][j-1], [i-1][j-1] and add 1 to it and update
# the current grid [i][j] with that (line 20). The reason to look at neighbours is because if neighbours are part of larger square then we append current 1 and update the bigger square by size 1.
# Keep track of maximum square value so far and at last return its square (area)

class Solution(object):
    def maximalSquare(self, matrix):
        max_dim, d1  = 0, len(matrix)
        
        if d1 == 0:
            return 0
        else:
            d2 = len(matrix[0])
        
        for i in range(d1):
            for j in range(d2):
                matrix[i][j] = int(matrix[i][j])
                
                if not (matrix[i][j] == 0 or ((i-1)<0) or ((j-1)<0)):
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                max_dim = max(max_dim, matrix[i][j])
                
        return max_dim*max_dim