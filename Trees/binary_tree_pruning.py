# Link: https://leetcode.com/problems/binary-tree-pruning/

# Approach: Recursively iterate the tree nodes. For a given node, check whether either of its left or right subtree has 1 or not. If any of the tree has 1 absent in them (determined by message from
# those subtrees), then perform current_node.left = None or current_tree.right = None (tree pruning) depending on either left or right subtree is absent of 1 respectively. Finally return (ret1 or 
# ret2 or node.val), which sends the parent of current node the message that eother left subtree or right subtree or current node has 1 and thus do not prune it. Finally return root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recur(self, node):
        ret1, ret2 = 0, 0   # Stores messsage the left and right children return about presence or absence of 1 in them
        
        if node.left:
            ret1 = self.recur(node.left)
            if ret1 == 0:       # If sub tree has no instance of 1, then prune
                node.left = None
        
        if node.right:
            ret2 = self.recur(node.right)
            if ret2 == 0:       # If sub tree has no instance of 1, then prune
                node.right = None
                
        return (ret1 or ret2 or node.val)   # Sending back message that one of the subtree or current node has 1
    
    def pruneTree(self, root):
        _ = self.recur(root)    # Sending root for pruning
        return root