# Link: https://leetcode.com/problems/implement-strstr/

# Approach: Used Knuth-Morris-Prat Algorithm

class Solution(object):
    def strStr(self, t, s):
        last_match, s_index, t_index, NS, NT = -1, 0, 0, len(s), len(t)
        
        if s == "":
            return 0
        
        while t_index < NT:
            if last_match == -1 and s_index != 0 and t[t_index] == s[0]:
                last_match = t_index
            
            if t[t_index] == s[s_index]:
                s_index += 1
                t_index += 1
            else:                
                if t_index-last_match < s_index:
                    t_index, last_match = last_match, -1
                else:
                    last_match = -1
                    t_index += 1
                s_index = 0
                
            if s_index == NS:
                return t_index-NS            
        return -1