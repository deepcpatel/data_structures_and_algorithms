# Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Approach: Perform DFS in the tree. At each node, obtain maximum and minimum value from left and right chilld. Decide minimum value at current level out of lmax, rmax and current_value and simlarly for
# maximum at current level. Calculate absolute difference between (minimum and current value) and (maximum and current value). Compare it eith current maximum absolute difference so far and update if
# any difference is greater that that. Finally return the maximum absolute difference so far.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node):
        lmax, lmin, rmax, rmin = float('-inf'), float('inf'), float('-inf'), float('inf')
        
        if node.left:
            lmax, lmin = self.dfs(node.left)
        
        if node.right:
            rmax, rmin = self.dfs(node.right)
            
        maxi, mini = max(lmax, rmax, node.val), min(lmin, rmin, node.val)
        self.max_diff = max(self.max_diff, abs(node.val-maxi), abs(node.val-mini))
        
        return maxi, mini
        
    def maxAncestorDiff(self, root):
        self.max_diff = -1
        self.dfs(root)
        
        return self.max_diff