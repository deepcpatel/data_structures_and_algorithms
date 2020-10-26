# Link: https://leetcode.com/problems/minimum-falling-path-sum/

# Approach: Start from 2nd row (index 1) let it be arr[i][j]. Now for each element in that row, select either left (arr[i-1][j-1]), right (arr[i-1][j+1]) or above element (ar[i-1][j]) in previous row which is minimum and add it to current element. Follow same till last row and 
# return minimum element from last row.

class Solution(object):
    def minFallingPathSum(self, A):
        N = len(A)
        
        for i in range(1, N):
            for j in range(N):
                A[i][j] += min(A[i-1][j], A[i-1][j-1] if j-1>=0 else float('inf'), A[i-1][j+1] if j+1<N else float('inf'))
                
        return min(A[-1])
