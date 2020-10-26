# Link: https://leetcode.com/problems/spiral-matrix-ii/


class Solution(object):
    def generateMatrix(self, n):
        columns, rows = n, n
        sr, sc = 0, 0
        ans = []
        number = 1
        min_c, max_c, min_r, max_r = -1, n, -1, n
        
        for i in range(n):
            ans.append([0]*n)
        
        while number <= n*n:
            while sc < max_c and number <= n*n:
                ans[sr][sc] = number
                number += 1
                sc += 1
            
            min_r += 1
            sc -= 1
            sr += 1
            
            while sr < max_r and number <= n*n:
                ans[sr][sc] = number
                number += 1
                sr += 1
            
            max_c -= 1
            sr -= 1
            sc -= 1
            
            while sc > min_c and number <= n*n:
                ans[sr][sc] = number
                number += 1
                sc -= 1
                
            max_r -= 1
            sc += 1
            sr -= 1
            
            while sr > min_r and number <= n*n:
                ans[sr][sc] = number
                number += 1
                sr -= 1
                
            min_c += 1
            sr += 1
            sc += 1
            
        return ans