# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Approach: Simple Tree traversal and recording depth at every level

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def explore(self, node, depth):
        if self.maxd < depth:
            self.maxd = depth
        
        if node.left:
            self.explore(node.left, depth+1)
        
        if node.right:
            self.explore(node.right, depth+1)
            
    def maxDepth(self, root):
        self.maxd = 0
        if root:
            self.explore(root, 1)
        
        return self.maxd