# Link: https://leetcode.com/problems/cousins-in-binary-tree/

# Approach: Resursively traverse a tree with level and parent of the current node as the argument. If the node is one of the X or Y, then store its parents and depth 
# in a dictionary. Finally compare both the values and return True and False.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if x == y:      # Same nodes and not cousins, since all tree nodes are different
            return False
        
        ddic, pdic = {x:-1, y:-1}, {x:0, y:0}    # To store depth
        
        def recur(node, parent, depth):
            if node.left:
                recur(node.left, node.val, depth+1)
            
            if node.right:
                recur(node.right, node.val, depth+1)

            if node.val in ddic:
                ddic[node.val] = depth
                pdic[node.val] = parent
        
        recur(root, -1, 0)
        return ddic[x] == ddic[y] and pdic[x] != pdic[y]