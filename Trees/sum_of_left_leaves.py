# Link: https://leetcode.com/problems/sum-of-left-leaves/

# Approach: Traverse the tree using BFS. For each node entered in the queue, add its orientation as well. For example if it is left child, then add (n, -1) to the queue, it it is center, then add
# (n, 0) and if it is right child, add (n, 1) to the queue. After popping every node from the queue, check whether it is left node and it is a leaf node or not. If both the conditions are satisfied
# then ad its value to sum variable (here s). Finally return sum variable.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def sumOfLeftLeaves(self, root):
        
        if not root:
            return 0
        
        queue, s = deque([(root, 0)]), 0
        
        # Orientation: -1-> left, 0 -> center, 1 -> right
        
        while queue:
            n, orientation = queue.popleft()
            
            if (orientation  == -1) and (not (n.left or n.right)):    #  If this is true, then the node is the left leaf node
                s += n.val

            if n.left:
                queue.append((n.left, -1))
                                         
            if n.right:
                queue.append((n.right, 1))
        return s 