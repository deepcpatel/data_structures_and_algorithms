# Link: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Approach: Used dreal time merging of elements from two trees. Used iterative inorder traversal of trees and retrieved elements in sorted fashion from both the trees. At each loop iteration, the
# elements will be stored in array in the merged fashion.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):            
    def getAllElements(self, root1, root2):
        def inorder(stack):   # Inorder traversal in iterative way to get command of each iteration
            while 1:
                if stack[-1].left:
                    stack.append(stack[-1].left)
                    stack[-2].left = None
                else:
                    node = stack.pop()

                    if node.right:
                        stack.append(node.right)

                    return node.val
        
        stack_1, stack_2, ans = ([root1] if root1 else []), ([root2] if root2 else []), []
        temp_val_1 = (inorder(stack_1) if stack_1 else float('inf'))
        temp_val_2 = (inorder(stack_2) if stack_2 else float('inf'))
        
        while temp_val_1 != float('inf') or temp_val_2 != float('inf'):     # Dynamically merging the elements
            if temp_val_1 < temp_val_2:
                ans.append(temp_val_1)
                
                temp_val_1 = (inorder(stack_1) if stack_1 else float('inf'))
            elif temp_val_1 == temp_val_2:
                ans.append(temp_val_1)
                ans.append(temp_val_2)
                
                temp_val_1 = (inorder(stack_1) if stack_1 else float('inf'))
                temp_val_2 = (inorder(stack_2) if stack_2 else float('inf'))
            else:
                ans.append(temp_val_2)
                
                temp_val_2 = (inorder(stack_2) if stack_2 else float('inf'))
        
        return ans