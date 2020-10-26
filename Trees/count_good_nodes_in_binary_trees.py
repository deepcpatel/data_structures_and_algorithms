# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Approach: Traverse the tree using DFS. Keep a maximum variable, which stores the max value seen so far in the path. At each node, if the node.val is greater than max_value, then increment good_nodes
# variable and asign the new max_value = node.val for the remaining path. Then visit the left child and right child of the current node. Finally return the good_nodes after traversing the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, max_far):
        if node.val >= max_far:
            max_far = node.val
            self.good_nodes += 1
        
        if node.left:
            self.dfs(node.left, max_far)
            
        if node.right:
            self.dfs(node.right, max_far)
        
    def goodNodes(self, root):
        self.good_nodes = 0
        self.dfs(root, float('-inf'))
        return self.good_nodes