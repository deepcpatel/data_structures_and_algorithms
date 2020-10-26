# Link: https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Approach: Perform DFS on a tree. For each left nad right child, get how much coins (returns negative output usually) does it need to fullfill him and their child (however, if they have extra, 
# they can return you positive sum back). Add those return values (their absolute) in the counter since that much money will be transferred thus that many steps will be taken.  Finally return the 
# total money currently + left child requirement + right child requirement - 1 back (this value will be negative or positive depending whether left child and right child gives us money or takes from us
# respectively. Moreover, it also depends on the money we have currently).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node):
        lborrow, rborrow = 0, 0
        
        if node.left:
            lborrow = self.dfs(node.left)
            
        if node.right:
            rborrow = self.dfs(node.right)
            
        self.total_count += abs(lborrow) + abs(rborrow)
            
        return node.val + lborrow + rborrow - 1

    def distributeCoins(self, root):
        self.total_count = 0
        self.dfs(root)
        
        return self.total_count