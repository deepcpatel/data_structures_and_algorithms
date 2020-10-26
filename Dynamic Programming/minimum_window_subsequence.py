# Link: https://www.lintcode.com/en/old/problem/minimum-window-subsequence/

# Approach: Video: https://www.youtube.com/watch?v=W2DvQcDPD9A. Basically, match all the characters in T along with characters in S. Then perform backward matching of that. Note the total length and proceed to 
# the end of S.

class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        i, j, N, M, end, min_d, window = 0, 0, len(S), len(T), -1, float('inf'), ""
        
        while i<N:
            
            if S[i] == T[j]:
                j += 1
            
            if j == M:
                end, j = i, j-1
                
                while j >= 0:
                    if S[i] == T[j]:
                        j -= 1
                    i -= 1
                
                i, j = i+1, j+1
            
                if end-i+1 < min_d:
                    min_d = end-i+1
                    window = S[i:end+1]
            i += 1
        
        return window