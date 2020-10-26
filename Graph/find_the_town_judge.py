# Link: https://leetcode.com/problems/find-the-town-judge/

# Approach: Store in-links and out-links corresponding to each number in a list. Return a number with N-1 in-links and 0 out-links, else return -1.

class Solution(object):
    def findJudge(self, N, trust):
        in_list, out_list = [0]*N, [0]*N
        
        for e in trust:
            in_list[e[1]-1] += 1
            out_list[e[0]-1] += 1
            
        for i in range(N):
            if in_list[i] == N-1 and out_list[i] == 0:
                return i+1
        return -1 