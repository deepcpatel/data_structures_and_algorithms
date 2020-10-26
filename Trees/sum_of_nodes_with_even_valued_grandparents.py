# Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Approach: Maintain a set in which you record the level of nodes to be added. Now itertate tree using DFS and at every even node add current_tree_level+2 into set. Also check whether current_level
# is in set, if it is, then add node value into total sum. After iterating left and right children, remove level+2 from the set so that it does not interfere with nodes at same level in other tree
# branch.  

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, level):
        if level in self.level_set:
            self.sum += node.val
            
        if node.val%2 == 0:
            self.level_set.add(level+2)
        
        if node.left:
            self.dfs(node.left, level+1)
                
        if node.right:
            self.dfs(node.right, level+1)
            
        if node.val%2 == 0:
            self.level_set.remove(level+2)
    
    def sumEvenGrandparent(self, root):
        self.sum, self.level_set = 0, set()
        self.dfs(root, 0)
        return self.sum 