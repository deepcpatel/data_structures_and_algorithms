# Link: https://leetcode.com/problems/convert-bst-to-greater-tree/

# Approach: Traverse tree from right to left and accumulate sum of all the right elements (since it is greater than current node). Add that to the current node and 
# then visit the left tree to do the same. Finally return the node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def traverse_tree(self, node):
        
        if node.right:
            self.traverse_tree(node.right)
        
        node.val += self.sum
        self.sum = node.val
        
        if node.left:
            self.traverse_tree(node.left)
    
    def convertBST(self, root):
        self.sum = 0
        
        if root:
            self.traverse_tree(root)
            
        return root