# Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Approach: The tree structure helps us generate the pattern to find second minimum node. At every step, we would have three conditions - (1). right.val == left.val == min_val, (2). right.val
# < left.val and right.val == min_val and (3). left.val < right.val and left.val == min_val. We will explore the node which is == min_val either it is left node or right node or both. For second
# and third contition above, we will either assign self.second_min = min(node.left.val, self.second_min) or self.second_min = min(node.right.val, self.second_min) respectively. Finally we return 
# self.second_min value or -1 if second_min is unchanged to its initial value. Also, min_val is the minimum value which is root.val

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def step_traverse(self, node):
        if node.left and node.right:                   
            if node.right.val == node.left.val == self.min:
                self.step_traverse(node.right)
                self.step_traverse(node.left)
            elif node.right.val == self.min:
                self.second_min = min(node.left.val, self.second_min)
                self.step_traverse(node.right)
            elif node.left.val == self.min:
                self.second_min = min(node.right.val, self.second_min)
                self.step_traverse(node.left)
        
    def findSecondMinimumValue(self, root):
        
        if not root or not root.left:
            return -1
        
        self.second_min, self.min = float('inf'), root.val
        self.step_traverse(root)
        
        if self.second_min == float('inf'):
            return -1
        
        return self.second_min