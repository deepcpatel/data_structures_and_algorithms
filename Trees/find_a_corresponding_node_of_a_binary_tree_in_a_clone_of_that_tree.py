# Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Approach: Iterate both the binary tree using DFS simultaneously and when the node of first tree is equal to target value, return the cloned node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, a1, a2, target):        
        if a1 == target:
            return a2
        else:
            r1, r2 = None, None
            
            if a1.left:
                r1 = self.dfs(a1.left, a2.left, target)
                
            if a1.right:
                r2 = self.dfs(a1.right, a2.right, target)
            
            return (r1 if r1 != None else r2)
        
    def getTargetCopy(self, original, cloned, target):
        return self.dfs(original, cloned, target)