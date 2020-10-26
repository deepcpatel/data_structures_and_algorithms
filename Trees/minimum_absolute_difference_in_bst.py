# Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Approach: The solution is based on fact that in a sorted array, you can find minimum difference only between two adjacent pairs of numbers. If two non adjacent numbers are subtracted then the 
# absolute difference will be guaranteed greater than the minimum absolute difference possible in the array. Now in a BST, the sorted array can be simulated using in-order traversal. So here, we
# did inorder traversal and found difference between previous node val and current value and checked whether it is globally minimum by min(self.min_diff, node.val - self.prev_val). Finally return
# the minimum difference.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recur_traverse(self, node):
        if node.left:
            self.recur_traverse(node.left)

        self.min_diff, self.prev_val = min(self.min_diff, node.val - self.prev_val), node.val
        
        if node.right:
            self.recur_traverse(node.right)
                
    def getMinimumDifference(self, root):
        self.min_diff, self.prev_val = float('inf'), float('-inf')
        self.recur_traverse(root)
        return self.min_diff 