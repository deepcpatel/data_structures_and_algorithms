# Link: https://leetcode.com/problems/balanced-binary-tree/

# Approach: Traverse the tree using DFS. At each node obtain whether its left and right child tree are balanced and what is their maximum heights. Now using this information calculate whether
# current tree is balanced using abs(left_height - right_height)<=1 condition. Now perform and operation between child's results and current condition results and return them along with maximum
# height of current tree [max(left_height+1, right_height+1)].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def check_balanced_trees(self, node):
        h1, h2, balanced = 0, 0, True
        
        if node.left:
            balanced, h1 = self.check_balanced_trees(node.left)
        
        if balanced and node.right:
            balanced, h2 = self.check_balanced_trees(node.right)
        
        return (balanced and abs(h1 - h2)<=1), max(h1+1, h2+1) 
        
        
    def isBalanced(self, root):
        if not root:
            return True
        
        balanced, _ = self.check_balanced_trees(root)
        return balanced