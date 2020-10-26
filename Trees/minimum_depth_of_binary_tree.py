# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Approach 1: Use DFS to traverse the tree and keep track of level variable. Now at each leaf node (no left or right child) check whether min_level is greater then level. If true then update it with
# level. Finally return the min_level.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, level):
        if not (node.left or node.right):   # Leaf node
            self.min_level = min(level, self.min_level)
        
        if node.left:
            self.dfs(node.left, level + 1)
        
        if node.right:
            self.dfs(node.right, level + 1)
        
    def minDepth(self, root):
        if not root:
            return 0
        
        self.min_level = float('inf')
        self.dfs(root, 1)
        return self.min_level 

# Approach 2 (Faster): Use BFS to traverse the tree and return the current depth level as soon as you encounter a leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):        
    def minDepth(self, root):
        if not root:
            return 0
        
        queue, depth = deque([root]), 1
        
        while queue:
            q_len = len(queue)
            
            while q_len>0:
                node = queue.popleft()
                q_len -= 1
                
                if not (node.left or node.right):
                    return counter

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            depth += 1  # Updating depth after all nodes of current depth level are dealth with