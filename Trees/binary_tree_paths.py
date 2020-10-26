# Link: https://leetcode.com/problems/binary-tree-paths/

# Approach: Traverse the tree using DFS. At each node check whether there is left or right child. If both are absent, then it is leaf node and we can complete tha path string by appending current value
# and update the ans_list. If there is any of the left or right child, then call them using DFS nad pass the updated path string as previous_str + str(current_val) + "->". Finally return the list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def get_path(self, node, string):   # DFS
        if not node.left and not node.right:    # Checking for leaf node
            self.ans_list.append(string + str(node.val))
        
        if node.left:
            self.get_path(node.left, string+str(node.val)+"->")
            
        if node.right:
            self.get_path(node.right, string+str(node.val)+"->")
        
    def binaryTreePaths(self, root):
        self.ans_list = []
        
        if root:
            self.get_path(root, "")
        return self.ans_list