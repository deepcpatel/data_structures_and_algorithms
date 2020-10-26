# Link: https://leetcode.com/problems/subtree-of-another-tree/

# Approach: Perform Pre-order traversal of both the Trees and compare the node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compare_nodes(self, t1, t2):
        v1, v2 = False, False
        
        if t1.val == t2.val:
            if t2.left == None and t1.left == None:
                v1 = True
            elif t2.left == None or t1.left == None:
                v1 = False
            else:
                v1 = self.compare_nodes(t1.left, t2.left)
                
            if t2.right == None and t1.right == None:
                v2 = True
            elif t2.right == None or t1.right == None:
                v2 = False
            else:
                v2 = self.compare_nodes(t1.right, t2.right)
            
        return (v1 and v2)
    
    def pre_traverse(self, t1, t2):
        if self.compare_nodes(t1, t2):
            return True
        
        if t1.left != None:
            if self.pre_traverse(t1.left, t2):
                return True
            
        if t1.right != None:
            if self.pre_traverse(t1.right, t2):
                return True
        
        return False
                
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.pre_traverse(s, t)