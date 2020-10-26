# Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Approach: Reconstruct Binary Tree using DFS. Recursively go to each child node and update the value using the convention given in the tree. At every node, add its value to the set so that element 
# searching becomes in O(1). During find operation, just check whether target element is in the set or not and eturn the answer accordingly.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements(object):
    
    def __init__(self, root):
        # Recover Tree
        self.el_dict = set()
        
        if root != None:
            root.val = 0
            self.dfs(root)

    def dfs(self, node):
        self.el_dict.add(node.val)
        
        if node.left:
            node.left.val = 2*node.val + 1
            self.dfs(node.left)
        
        if node.right:
            node.right.val = 2*node.val + 2
            self.dfs(node.right)
        
    def find(self, target):
        return target in self.el_dict
        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)