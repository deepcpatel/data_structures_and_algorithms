# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Approach: See the current value. If it is greater than root, recursively call insertIntoBST with right child as new root, else do the same for left child. If find that right or left child is None
# Insert the new node there, no need to recursively call subtrees, as they does not exist.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        
        return root