# Link: https://leetcode.com/problems/increasing-order-search-tree/

# Approach: Perform inorder traversal and append each node in the list. Now after the traversal is finished, iterate in the list and ling right of each node to its
# next node and left to the None. Return the first element of the list as itis the top node of the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorder_traversal(self, node):
        temp = None
        
        if node:
            self.inorder_traversal(node.left)
            self.node_li.append(node)
            self.inorder_traversal(node.right)
        
    def increasingBST(self, root):
        self.node_li = []
        self.inorder_traversal(root)
        self.node_li.append(None)
        
        for i in range(len(self.node_li)-1):
            self.node_li[i].right, self.node_li[i].left = self.node_li[i+1], None
        
        return self.node_li[0]