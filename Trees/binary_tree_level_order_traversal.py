# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Approach: Recursion. At each level of tree add new ist to final answer and add elements of those levels into corresponding sublist. Index each sublist by current tree leve;.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def explore(self, node, level):
        if node:
            if len(self.ans) < level:
                self.ans.append([])
            self.ans[level-1].append(node.val)
            self.explore(node.left, level+1)
            self.explore(node.right, level+1)
            
    def levelOrder(self, root):
        self.ans = []
        self.explore(root, 1)
        return self.ans