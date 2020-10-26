# Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Approach: Recursively traverse the tree and also keep a level variable. If you iterate child, perform level+1. At each point, see if level == len(ans_list).
# If it is, then our list needs one more sub list as new level is found. Then, add the element at sub list by li[-(level+1)].append(node.val). Now, since here is 
# reverse level order, we will use deque and add the sublist from left. We ill index each sub list by ans_list[-(level+1)], i.e. from the end. Finally we return the ans_list (here li).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        li = deque()
        
        def recur(level, node):
            if len(li)<=level:
                li.appendleft([])
            
            li[-(level+1)].append(node.val)
            
            if node.left:
                recur(level+1, node.left)
            
            if node.right:
                recur(level+1, node.right)
                
        if root:
            recur(0, root)
        return li