# Link: https://leetcode.com/problems/symmetric-tree/

# Approach: The code is recursive and main condition is in line 20. Each recursion (1). takes one node from left sub part of root and right subpart of root, (2). compares them and (3). their left
# and right child respectively and vice-versa. Moreover, each recursion ensures comparison of their respective nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def itr(self, n1, n2):
        if n1 == n2 and n1 == None:
            return True
        if n1 == None or n2 == None:
            return False
        else:
            return (n1.val == n2.val) and self.itr(n1.left, n2.right) and self.itr(n1.right, n2.left)
    
    def isSymmetric(self, root):
        if root:
            return self.itr(root.left, root.right)
        return True 
