# Link: https://leetcode.com/problems/deepest-leaves-sum/

# Approach: Iterate the tree using BFS. At each level calculate the sum of all the nodes (and reset it at the beginning of the new level). Return the sum of nodes after visiting the final level.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def deepestLeavesSum(self, root):
        queue, sums = deque([root]), 0
        
        while queue:
            cur_len, sums = len(queue), 0
            
            while cur_len !=0:          # This loop helps to differentiate between levels in BFS
                n = queue.popleft()
                sums += n.val
                
                if n.left:
                    queue.append(n.left)
                
                if n.right:
                    queue.append(n.right)
                
                cur_len -= 1
                
        return sums