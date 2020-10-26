# Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Approach: This is basically DFS exploration of the tree. However, add the current node to the list after traversing the children.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def traverse(self, node):
        if node:        
            for c in node.children:
                self.traverse(c)
            
            self.ans.append(node.val)
        
    def postorder(self, root):
        self.ans = []
        self.traverse(root)
        return self.ans