# Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/

# Approach: Basically, we initially add all ones. Now, for each cell matrix[i][j] which equals one, we do matrix[i][j] = matrix[i][j] + min(left_val, upper_val, upper_left_val). Why this is so because
# we see that the current square will form if it is guaranteed that all the squares having one size smaller are already formed. If one of them is not there (eg, 2, 2, 1), then there is one square which is
# zero and thus becoming a hole in potential 3x3 square.

class Solution(object):
    def countSquares(self, matrix):
        init_sum, m, n = sum([sum(matrix[i]) for i in range(len(matrix))]), len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    init_sum += matrix[i][j] - 1
        return init_sum