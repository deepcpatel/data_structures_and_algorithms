# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Approach: Make middle element of an array to be tree node. Now assign left node and right nodes as middle nodes of left half and right half of the array respectively. Do this operation recursively
# to form a binary search tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def recur_binary(self, start, end):
        tree_node = None
        
        if start<=end:
            mid = (start + end)//2
            tree_node = TreeNode(self.nums[mid])
            
            tree_node.left = self.recur_binary(start, mid-1)
            tree_node.right = self.recur_binary(mid+1, end)
        return tree_node    
        
    def sortedArrayToBST(self, nums):
        self.nums = nums
        return self.recur_binary(0, len(nums)-1)