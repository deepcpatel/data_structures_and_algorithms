# Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/ 

# Approach: Traverse the tree using the DFS. At each step append the current value in the string and at the leaf nodes convert that string to integer and add it to current sum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, stri):
        if node.left:
            self.dfs(node.left, stri+str(node.val))

        if node.right:
            self.dfs(node.right, stri+str(node.val))
        
        if not (node.left or node.right):   # Leaf node
            self.ans += int(stri+str(node.val), 2)
            
    def sumRootToLeaf(self, root):
        self.ans = 0
        self.dfs(root, '0b')
        return self.ans