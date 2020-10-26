# Link: https://leetcode.com/problems/construct-string-from-binary-tree/

# Approach: Traverse the tree recursively using DFS and append node value to the string. Then visit left, but before that add "(" and after visiting add ")" to string. Similarly for right. However, 
# if left is NULL and if right is not NULL then add "()" to the string in order to keep node to value mapping from tree and string. Return the string finally.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):

    def recur_str(self, node):
        self.s += str(node.val)
        
        if node.left:
            self.s += "("
            self.recur_str(node.left)
            self.s += ")"
        elif node.right:
            self.s += "()"
        
        if node.right:
            self.s += "("
            self.recur_str(node.right)
            self.s += ")"
    
    def tree2str(self, t):
        self.s = ""
        
        if t:
            self.recur_str(t)
        return self.s