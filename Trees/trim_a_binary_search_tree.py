# Link: https://leetcode.com/problems/trim-a-binary-search-tree/

# Approach: Traverse the BST and look at node values. If node.value > R, then we need to discard that node and its right branch, as all elements in it will also be greater than R. Thus replace node with 
# its left child. Similarly, if node.value < L, remove left branch and replace node with its right child. If node.value is between L and R, then recursively explore its left nad right children for 
# the constraints.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def explore_and_trim(self, node, L, R):
        
        if node:
            if node.val > R:
                return self.explore_and_trim(node.left, L, R)
            elif node.val < L:
                return self.explore_and_trim(node.right, L, R)

            node.right = self.explore_and_trim(node.right, L, R)
            node.left = self.explore_and_trim(node.left, L, R)

        return node
        
    def trimBST(self, root, L, R):
        return self.explore_and_trim(root, L, R)