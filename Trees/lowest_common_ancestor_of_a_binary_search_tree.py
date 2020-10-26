# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Approach: Traverse the tree nodes to search for p and q in the tree. At each node, track whether it is <, ==, or > the each of p and q. Based on that determine next nodes for both p and q. 
# If the next nodes for both p and q are different then we know this is where the path diverge and thus the deepest common ancestor is the current node. Thus return that. If next nodes are 
# same for both of them, then further traverse the tree with next mode.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Here Lowest means the deepest node (not the smallest)

class Solution(object):
    def traverse_tree(self, p, q, node):        
        if node.val < p:
            pnext = node.right
        elif node.val == p:
            pnext = None
        else:
            pnext = node.left

        if node.val < q:
            qnext = node.right
        elif node.val == q:
            qnext = None
        else:
            qnext = node.left

        if pnext and qnext and pnext == qnext:      # Checking whether next path of both nodes are same. If not then return current node as common ancestor
            return self.traverse_tree(p, q, pnext)
        else:
            return node
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        return self.traverse_tree(p.val, q.val, root)