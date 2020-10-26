# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Approach: Following method is the iterative approach for inorder traversal using Stack. Basically, add all the left child of top stack nodes back to stack. After no left child is there, add the
# pop the top node, print its value (or save to an array) and add its right child on top of stack. Repeat this until the stack is empty. Can also be solved by Morris Traversal using O(1) memory and 
# O(n) runtime.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        
        stack, ans = [root], []
        
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None
            else:
                node = stack.pop()
                ans.append(node.val)
                
                if node.right:
                    stack.append(node.right)
        
        return ans