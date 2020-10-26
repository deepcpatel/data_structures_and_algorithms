# Link: https://leetcode.com/problems/invert-binary-tree/

# Approach: Traverse through the tree using DFS. Now at each node exchange left nad right nodes. and if either  of them is not None, append it to the stack to explore
# them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        stack = ([root] if root else [])
        
        while stack:
            node = stack.pop()
            
            node.right, node.left = node.left, node.right

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return root