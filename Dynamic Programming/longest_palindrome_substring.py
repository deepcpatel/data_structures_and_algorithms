# Link: https://leetcode.com/problems/longest-palindromic-substring/ 

# Explanation:
# We will go to each element in array using for loop and determine whether it is a central element of some palindrome
# by comparing neighbouring characters. If it is palindrome, then we expand palindrome (if possible) using while loop on both the sides.
# And we store beginning and end index of the palindrome with max_length

class Solution(object):
    def longestPalindrome(self, s):
        
        if s == "":
            return ""
        
        n = len(s)
        s = s+ "-"
        max_len, m_s, m_e = -1, 0, 0
        
        for i in range(1, n):
            if s[i-1] == s[i+1]:
                start = i
                end = i

                while 1:
                    if start>0 or end<n-1:
                        if s[start-1] == s[end+1]:
                            start -= 1
                            end += 1
                        else:
                            break
                    else:
                        break

                length = end-start+1
                if max_len < length:
                    max_len = length
                    m_s = start
                    m_e = end
                
            if s[i] == s[i-1]:
                start = i-1
                end = i
                while 1:
                    if start>0 or end<n-1:
                        if s[start-1] == s[end+1]:
                            start -= 1
                            end += 1
                        else:
                            break
                    else:
                        break
                        
                length = end-start+1
                if max_len < length:
                    max_len = length
                    m_s = start
                    m_e = end
                    
        return s[m_s:m_e+1]