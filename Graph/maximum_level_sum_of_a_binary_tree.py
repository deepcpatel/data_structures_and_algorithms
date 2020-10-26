# Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Approach: First solution is DFS based. Recursively visit each level and add all elements into a corresponding location in dictionary. Finally, search in dictionary for smallest element.
# BFS solution which is much faster is possible.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS Solution
class Solution(object):
    def explore_levels(self, level, node):
        if node!= None:
            self.l_dict[level] = self.l_dict.get(level, 0) + node.val
            self.explore_levels(level+1, node.left)
            self.explore_levels(level+1, node.right)
                   
    def maxLevelSum(self, root):
        self.l_dict = {}
        self.explore_levels(1, root)
        max_val, max_key = float('-inf'), -1
        
        for k in self.l_dict.keys():
            if self.l_dict[k]>max_val:
                max_val = self.l_dict[k]
                max_key = k
        return max_key

'''
# BFS Solution
import collections 

class Solution(object):                   
    def maxLevelSum(self, root):
        max_val, max_key = float('-inf'), -1
        node_q = collections.deque([root])
        level, q_size, sums = 1, len(node_q), 0
        
        while q_size != 0:
            el = node_q.popleft()
            sums += el.val
            q_size -= 1
            
            if el.left:
                node_q.append(el.left)
            
            if el.right:
                node_q.append(el.right)
        
            if q_size == 0:
                if max_val < sums:
                    max_val = sums
                    max_key = level
                sums = 0
                level += 1
                q_size = len(node_q)
        
        return max_key
'''