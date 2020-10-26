# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

# Approach: If node value is not equal to given value then move left if given value is smaller than node value or else move right if it is greater.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        ret = root
        
        while ret:
            if ret.val == val:
                return ret
            elif val > ret.val:
                ret = ret.right
            else:
                ret = ret.left
        
        return ret