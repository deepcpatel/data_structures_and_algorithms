# Link: https://leetcode.com/problems/binary-tree-tilt/submissions

# Approach: Traverse the tree using DFS and at every level return the left_child_tree_sum + right_child_tree_sum + node.val (sum of children nodes) and left_child_tile + right_child_tilt + 
# abs(left_child_tree_sum - right_child_tree_sum). Finally return the final tilt.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def find_tilt(self, node):
        sm1, sm2, df1, df2 = 0, 0, 0, 0
        
        if node.left:
            sm1, df1 = self.find_tilt(node.left)
        
        if node.right:
            sm2, df2 = self.find_tilt(node.right)
        
        return sm1 + sm2 + node.val, abs(sm2-sm1) + df1 + df2 
        
    def findTilt(self, root):
        if not root:
            return 0
        
        sm, tilt = self.find_tilt(root)
        return tilt