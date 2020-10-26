# Link: https://leetcode.com/problems/maximum-binary-tree/

# Approach: O(n) Solution. We make a stack which stores the nodes of the tree so far (or visited elements). Each element in the stack is right child of the previous element in the stack. We start 
# iterating the array from left to right. When a new element is in hand, we check whether it is greater than the top element in the stack, if so, then we pop the top elements until the current element
# is smaller than the new top element. After that, we make previous top element, the left child of current element and current element the right child of the new top element. Then we append the current 
# element at the top of the stack. We continue till we have iterated all the array elements from left to right. Fianlly, we return the first (bottom) element from the stack, since, it will be the maximum
# element and the root node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0:
            return None
        
        stack = []  # Holds the Tree
        
        for n in nums:
            node, tmp = TreeNode(val=n), None

            while stack and stack[-1].val < node.val:
                tmp = stack.pop()
            
            if tmp:
                node.left = tmp
            
            if stack:
                stack[-1].right = node
            
            stack.append(node)
        
        return stack[0]
        
'''
# Slower code using recursion - O(n^2)

class Solution(object):
    def find_max_idx(self, arr, start, end):
        max_n, max_idx = float('-inf'), -1
        
        for i in range(start, end):
            if max_n < arr[i]:
                max_n, max_idx = arr[i], i
        
        return max_idx
        
    def build_max_tree(self, arr, start, end):
        max_idx = self.find_max_idx(arr, start, end)
        new_node = TreeNode(val=arr[max_idx])

        if max_idx>start:
            new_node.left = self.build_max_tree(arr, start, max_idx)

        if (end-1)>max_idx:
            new_node.right = self.build_max_tree(arr, max_idx+1, end)

        return new_node       
        
    def constructMaximumBinaryTree(self, nums):
        return self.build_max_tree(nums, 0, len(nums))
'''