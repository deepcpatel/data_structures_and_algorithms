# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Approach: Iterate over every node using DFS. Visit the left and right child and get the maximum size pf path under them. Add those maximum path and assign that to self.max_path if it is greater 
# then its current value. Finally return the max(left_path+1, right_path+1) from dfs(). This represents maximum length of path under the current node. The self.max_path would be the final answer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node):
        s1, s2 = 0, 0
        
        if node.left:
            s1 = self.dfs(node.left)
        
        if node.right:
            s2 = self.dfs(node.right)
            
        self.max_path = max(self.max_path, s1 + s2)
        
        return max(s1+1, s2+1)
        
    def diameterOfBinaryTree(self, root):
        self.max_path = 0
        
        if root:
            self.dfs(root)
        return self.max_path