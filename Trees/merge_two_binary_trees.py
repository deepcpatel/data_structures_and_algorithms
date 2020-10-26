# Link: https://leetcode.com/problems/merge-two-binary-trees/

# Approach: Using DFS we can traverse both the trees and add their respective values and store it to a newly created node. Finally we will return that new node. We will not call recursion if both
# n1 and n2 are None.s

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):          
    
    def dfs(self, n1, n2):
            new_node = None
            if n1 or n2:
                new_node = TreeNode(0)

                if n1:
                    new_node.val += n1.val

                if n2:
                    new_node.val += n2.val

                new_node.left = self.dfs((n1.left if n1 else None), (n2.left if n2 else None))
                new_node.right = self.dfs((n1.right if n1 else None), (n2.right if n2 else None))
            return new_node            
    
    def mergeTrees(self, t1, t2):    
        return self.dfs(t1, t2)

'''
# Faster Solution: Don't create new node, just pass one of them back by updating the value. Otherwise DFS is the correct way.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):          
    
    def dfs(self, n1, n2):
            if not n1:
                return n2
            
            if not n2:
                return n1
            
            n1.val += n2.val
            n1.left, n1.right = self.dfs(n1.left, n2.left), self.dfs(n1.right , n2.right)
            return n1            
    
    def mergeTrees(self, t1, t2):    
        return self.dfs(t1, t2)
'''