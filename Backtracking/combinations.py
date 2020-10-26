# Link: https://leetcode.com/problems/combinations/

# Approach: Backtracking. We need combinations of the number. Let's say n = 5, k = 2, then we start from 1 in first recursion, from that we call another recursion starting from 2
# Before second recursion, append 1 in a list. In the second recursion recursion, append 2. We don't need third recursion as k = 2 or we only need two combinations. We then come back
# to first recursion function and again call second recursion function now starting from 3. After all combinations with one is over, we now need all combinations atrting from 2. Thus
# in the first recursion function, change start from 2 and follow the abpve steps. 
#
# Let's say, we subsequently come to 5 as start point in first recursion, then we don't need to call a recursion again, as we know that we don't have enough numbers left after 5 such that
# they form combinations of length k. Thus we stop calling second recursion from that. This condition is being taken care in line 18 below.


class Solution(object):
    def recur(self, start, n, rem_level, prev_list, ans_list):
        if rem_level > 0:
            for i in range(start, n+1):
                prev_list.append(i)
                
                if n-i >= rem_level-1:
                    self.recur(i+1, n, rem_level-1, prev_list, ans_list)
                prev_list.pop()
        else:
            ans_list.append(list(prev_list))
    
    def combine(self, n, k):
        ans_list = []
        self.recur(1, n, k, [], ans_list)
        return ans_list