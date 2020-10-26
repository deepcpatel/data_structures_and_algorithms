# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Approach: Perform BFS on tree and at each level accumulate the sum of each node. Average it out at last (when all nodes of levels are popped out from the queue). Store this in the answer list
# and return the list

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        queue, ans = deque([root]), []
        cur_len, num_el, avg_sum = len(queue), len(queue), 0.0
        
        while queue:
            node = queue.popleft()
            avg_sum += node.val
            cur_len -= 1
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
                
            if cur_len == 0:
                cur_len = len(queue)
                ans.append(avg_sum/num_el)
                avg_sum, num_el = 0.0, cur_len
        
        return ans