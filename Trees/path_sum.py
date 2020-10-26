# Link: https://leetcode.com/problems/path-sum/

# Approach: Traverse the tree using DFS. Cumulatively add the nodes of the tree to a variable. At the leaf node (having no child) check whether the sum is == target_sum. If it is then return True
# else return False.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, prev_sum, summ):
        curr_sum, ret1, ret2 = prev_sum + node.val, False, False
        
        if not (node.left or node.right):
            if curr_sum == summ:
                return True
            else:
                return False
        
        if node.left:
            ret1 = self.dfs(node.left, curr_sum, summ)
            
        if node.right:
            ret2 = self.dfs(node.right, curr_sum, summ)
        
        return (ret1 | ret2)
        
    def hasPathSum(self, root, summ):
        if not root:
            return False
        
        return self.dfs(root, 0, summ)