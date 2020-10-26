# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Approach: Start from Top Right corner of matrix. If target is greater that it, go down else go left. If equal to it, return True

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False
        
        columns = len(matrix[0])
        if columns == 0:
            return False
        
        start_r, start_c = 0, columns-1     # Top right Corner
        
        while start_r<rows or start_c >= 0:
            if target == matrix[start_r][start_c]:
                return True
            elif target > matrix[start_r][start_c]:
                if start_r<rows-1:
                    start_r += 1
                else:
                    return False
            elif target < matrix[start_r][start_c]:
                if start_c>0:
                    start_c -= 1
                else:
                    return False
        return False