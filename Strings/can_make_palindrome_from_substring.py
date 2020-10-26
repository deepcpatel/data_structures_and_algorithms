# Link: https://leetcode.com/problems/can-make-palindrome-from-substring/

from collections import defaultdict

# Counting the characters in substring and see how much edits are required. 
# For palindrome, atmost one character count must be odd
# Preprocessing string to extracter character count

class Solution(object):
    
    def canMakePaliQueries(self, string, queries):
        counter = 0
        temp = 0
        ans = []
        pos_li = [defaultdict(int)] * (len(string)+1)
        
        for i, c in enumerate(string):
            pos_li[i+1] = pos_li[i].copy()
            pos_li[i+1][c] += 1
        
        for q in queries:
            s, e, k = q[0], q[1], q[2]
            
            counter = 0
            temp = 0

            for a in pos_li[e+1].keys():
                temp = pos_li[e+1][a] - pos_li[s][a]
                
                if temp != 0 and temp%2 != 0:
                    counter += 1

            if int(counter/2) <= k:
                ans.append(True)
            else:
                ans.append(False)
        return ans