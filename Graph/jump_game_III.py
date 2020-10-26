# Link: https://leetcode.com/problems/jump-game-iii/submissions/

# Approach: BFS. Generate two child of current node i, that are i + arr[i] and i - arr[i]. Add them to queue and later visit them. Now, mark each visited cell as visited by -1. Whenever you visit cell
# with 0 value return True, else False.

from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        node_q, ar_len, a, b = deque([]), len(arr), start+arr[start], start-arr[start]
        
        if 0 <= a < ar_len:
            node_q.append(a)
            
        if 0 <= b < ar_len:
            node_q.append(b)
        
        while node_q:
            idx = node_q.popleft()
            
            if arr[idx] == 0:
                return True
            
            a, b, arr[idx] = idx+arr[idx], idx-arr[idx], -1

            if 0 <= a < ar_len and arr[a] != -1:
                node_q.append(a)
            
            if 0 <= b < ar_len and arr[b] != -1:
                node_q.append(b)

        return False 
