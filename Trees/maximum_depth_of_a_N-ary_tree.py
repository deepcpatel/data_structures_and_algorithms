# Link: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Approach: Recursively iterate the tree and keep a length counter at each level. Compare length counter with maximum so far at each iteration and return max_len at the
# end of the traversal.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def recur(self, node, length):
        if node:
            self.max_len = max(self.max_len, length)
            
            for c in node.children:
                self.recur(c, length+1)
        
    def maxDepth(self, root):
        self.max_len = 0
        self.recur(root, 1)
        return self.max_len