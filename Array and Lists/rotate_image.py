# Link: https://leetcode.com/problems/rotate-image/

# Approach: Transpose the image and reverse each row to rotate image 90 degrees

class Solution(object):
    def rotate(self, matrix):
        l = len(matrix)
        
        for i in range(l):
            for j in range(i, l):       # Transpose
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            for j in range(l//2):       # Reverse row
                matrix[i][j], matrix[i][l-j-1] = matrix[i][l-j-1], matrix[i][j]