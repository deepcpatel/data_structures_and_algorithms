# Link: https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Approach: We have to prune the leaf nodes and to-be leaf nodes (after pruning their children if required) having target values. Therefore, we can traverse the tree using DFS and at each iteration
# see whether the node is leaf node and having target value or not. If it is, the we return None, since we no more want that node or the node as it is if conditions are failed. Now update its parent
# with this new returned values (line 18 and 21). Finally return the root node after tree updation. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def dfs(self, node, target):        
        if node.left:
            node.left = self.dfs(node.left, target)
            
        if node.right:
            node.right = self.dfs(node.right, target)
            
        node = (None if not (node.left or node.right) and node.val == target else node)
        
        return node
        
    def removeLeafNodes(self, root, target):     
        return (self.dfs(root, target) if root else None)