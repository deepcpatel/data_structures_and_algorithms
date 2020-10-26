# Link: https://leetcode.com/problems/leaf-similar-trees/

# Approach: Traverse tree using DFS and add leaf node values in the string. Do this for both the roots and compare them at the end.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node):
        if not (node.left or node.right):
            self.str += str(node.val) + ","
            
        if node.left:
            self.dfs(node.left)
            
        if node.right:
            self.dfs(node.right)
            
    def leafSimilar(self, root1, root2):
        temp, self.str = "", ""
        
        self.dfs(root1)
        temp, self.str = self.str, ""
        self.dfs(root2)
        
        return temp == self.str