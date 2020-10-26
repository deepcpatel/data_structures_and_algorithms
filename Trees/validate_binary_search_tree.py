# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Approach: Traverse the tree and set the max and min condition of each left and right node value according to  lines 18, 19, 25 and 26

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def explore(self, node, minv, maxv):        
        if not (node.val>minv and node.val<maxv):
            return False
        
        if node.left:
            tmax = node.val
            tmin = minv
            ans = self.explore(node.left, tmin, tmax)
            if not ans:
                return False
            
        if node.right:
            tmax = maxv
            tmin = node.val
            ans = self.explore(node.right, tmin, tmax)
            if not ans:
                return False
            
        return True
    
    def isValidBST(self, root):
        ans = True
        if root:
            ans = ans and self.explore(root, float('-inf'), float('inf'))
        return ans