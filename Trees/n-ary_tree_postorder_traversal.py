# Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Approach: This is basically DFS exploration of the tree. However, add the node to the list first then traverse the children.

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
            self.ans.append(node.val)
        
            for c in node.children:
                self.traverse(c)            
        
    def preorder(self, root):
        self.ans = []
        self.traverse(root)
        return self.ans