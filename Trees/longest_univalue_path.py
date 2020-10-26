# Link: https://leetcode.com/problems/longest-univalue-path/

# Approach: Iterate the Tree in Post Order Traversal Fashion (or DFS). Make variables left_chain and right_chain in each iteration. These will store the left child path length and right child tree path 
# length (if they are contiguous path, else 0). DFs on left child will return chain_left and similarly for chain_right. Noew check whether the left child is same value as current node. If it is, then we
# want to extend the continuous path this increment chain_left else we want to break the path, thus make it zero. Similarly follow for right child. Now add both the variables to get the length of total 
# contiguous path chain (if it exist). Compare the current max_path_length with total_length and replace it if max_path_length is smaller than total_length. Finally return the max of chain_left and
# chain_right which will represent the longest contiguous univalue path from the current node to either of its child.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node):
        chain_left, chain_right = 0, 0
        
        if node.left:
            chain_left = self.dfs(node.left)
            
            if node.left.val != node.val:
                chain_left = 0
            else:
                chain_left += 1
        
        if node.right:
            chain_right = self.dfs(node.right)
            
            if node.right.val != node.val:
                chain_right = 0
            else:
                chain_right += 1
        
        total_chain = chain_left + chain_right
        self.max_len = max(self.max_len, total_chain)
        
        return max(chain_left, chain_right)

    def longestUnivaluePath(self, root):
        if not root:
            return 0
        
        self.max_len = float('-inf')
        self.dfs(root)
        return self.max_len