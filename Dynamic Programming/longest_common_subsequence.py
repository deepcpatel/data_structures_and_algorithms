# Link: https://leetcode.com/problems/longest-common-subsequence/

# Approach: Start with (M+1) x (N+1) matrix 'dp' (all cells initialized with zero). M = len(string1) and N = len(start2). Now, loop over all cells in the matrix (start from 1st row and 1st column,
# not 0th). Each [i][j] cell represents number of matches for string1[0 to i-1] and string2[0 to j-1]. For position [i][j] in the matrix, if string1[i-1] == string2[j-1] (i and j is 1 step back 
# in strings since we started iterating our matrix from 1), then it means we have a match, thus add 1 to whatever matches are at dp[i-1][j-1] and store in dp[i][j]. If there is no match then update
# current cell dp[i][j] with max(dp[i-1][j], dp[i][j-1]), whichever neighbouring has recorded highest matches. Finally, return the last element of the matrix.


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp_ar = [[0]*(n+1) for i in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp_ar[i][j] = dp_ar[i-1][j-1] + 1
                else:
                     dp_ar[i][j] = max(dp_ar[i][j-1], dp_ar[i-1][j])
        
        return dp_ar[-1][-1]