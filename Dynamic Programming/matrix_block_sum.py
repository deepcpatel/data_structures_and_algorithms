# Link: https://leetcode.com/problems/matrix-block-sum/

# Approach: Preprocess the matrix by adding sum of all elements till [i, j] as in line 12. Calculate max and min coordinates as in line 17 and 18. Now starting from that calculate sum as in line 25.

class Solution(object):
    def matrixBlockSum(self, mat, K):
        rows, columns, ans = len(mat), len(mat[0]), []
        
        # Preprocess
        for i in range(rows):
            for j in range(columns):
                mat[i][j] += (mat[i-1][j] if i else 0) + (mat[i][j-1] if j else 0) - (mat[i-1][j-1] if i and j else 0)
            ans.append([0]*columns)
        
        for i in range(rows):
            for j in range(columns):
                start_r, end_r = (i-K if (i-K)>=0 else 0), (i+K if (i+K)<rows else rows-1)
                start_c, end_c = (j-K if (j-K)>=0 else 0), (j+K if (j+K)<columns else columns-1)
                
                a = mat[end_r][end_c]
                b = (mat[end_r][start_c-1] if start_c else 0)
                c = (mat[start_r-1][end_c] if start_r else 0)
                d = (mat[start_r-1][start_c-1] if start_r and start_c else 0)
                
                ans[i][j] = a - b - c + d
        
        return ans