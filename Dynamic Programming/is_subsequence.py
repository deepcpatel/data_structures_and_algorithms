# Link: https://leetcode.com/problems/is-subsequence/

# Approach: Set a counter when s[counter] is equal to t[i]. This way we check all the characters of s if they are matching with characters in t. Finally, when counter == length_of_s, return True as we have
# successfully checked all the characters of s.

class Solution(object):
    def isSubsequence(self, s, t):
        NT, NS, counter = len(t), len(s), 0
        
        if NS == 0:
            return True
        
        for i in range(NT):
            if t[i] == s[counter]:
                counter += 1
            
            if counter == NS:
                return True
        
        return False