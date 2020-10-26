# Link: https://www.lintcode.com/problem/longest-common-substring/description

# Approach: Make a 2D array dp of size (m+1)*(n+1) where m == len(string1) and n == len(string2) and initialize with zero. Now start looping matrix from first column and first row. Each position dp[i][j]
# represents number of subsequent matches till now. If characters string[i-1] and string[j-1] matches then update a match at dp[i][j]  = dp[i-1][j-1] + 1. This meand from the previous position, we got
# a new match. At each match, measure the length of longest match till now by max_len = max(max_len, dp[i][j]). Finally return max_len.

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        m, n, max_len = len(A), len(B), 0
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len