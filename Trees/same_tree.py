# Link: https://leetcode.com/problems/same-tree/

# Approach: Recursive pre-order traversal of both the trees and at each recursion checking whether two passed argument nodes have equal value. Return True else return False.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if (p and q and p.val == q.val):
            return True & self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
        elif (p == q == None):
            return True
        else:
            return False