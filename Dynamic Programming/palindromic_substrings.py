# Link: https://leetcode.com/problems/palindromic-substrings/

# Approach: O(N^2) runtime. Got to ith character in the string and start expanding left and right of it if both the left and right characters matches. Expand till it exceeds string size or 
# corresponding left and right characters match no more. Take care of even and odd sized palindrome. For each palindrome found increment counter size and return.

class Solution(object):
    def palindrome_odd(self, i, N, s):
        left, right, count = i-1, i+1, 0
        
        while left>=0 and right<N and (s[left] == s[right]):
            count += 1
            left -= 1
            right += 1
               
        return count
    
    def palindrome_even(self, i, N, s):
        left, right, count = i, i+1, 0
        
        while left>=0 and right<N and (s[left] == s[right]):
            count += 1
            left -= 1
            right += 1
               
        return count
        
    def countSubstrings(self, s):
        pcount, N = len(s), len(s)
        
        for i in range(N):
            pcount += self.palindrome_odd(i, N, s)
            pcount += self.palindrome_even(i, N, s)
            
        return pcount