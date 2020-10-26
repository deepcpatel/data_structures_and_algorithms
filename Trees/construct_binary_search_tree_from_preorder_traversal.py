# Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Approach: Suboptimal solution. Use stack to store each node. Along with each node store the (min, max) limits of its left nad right sub trees. For 
# each node, if its value is between left (min, max) values of top stack node, make it left child of that top node, else if it satisfies right (min, 
# max) limits, make it right child of that top node. If noth the cases are not satisfied then pop the top value and start comprison with new top node.
# Finally, append the current node in stack with updated (min, max) limits.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        if len(preorder) == 0:
            return []
        
        stack = []
        
        for n in preorder:
            node = TreeNode(val=n)
            
            if not stack:
                stack.append((node, (float('-inf'), n), (n, float('inf')))) 
                continue
                             
            while not (stack[-1][1][0] < n < stack[-1][1][1] or stack[-1][2][0] < n < stack[-1][2][1]):
                stack.pop()
            
            low_limit, upper_limit = stack[-1][1], stack[-1][2]     # Min max limits of left and right sub trees
            
            if (low_limit[0] < n < low_limit[1]):
                stack[-1][0].left = node
                stack.append((node, (low_limit[0], n), (n, low_limit[1])))
            
            if (upper_limit[0] < n < upper_limit[1]):
                stack[-1][0].right = node
                stack.append((node, (upper_limit[0], n), (n, upper_limit[1])))
            
        return stack[0][0]
    
'''
# Optimal Solution (not mine)

# Approach: Recursively make the BST. Separate the nodes greater than current node and smaller than that. Now recursively call FormBSt on those two arrays
# Use root first element of array as the starting current node.

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # recursive
        if not preorder: return None
        root = TreeNode(val=preorder[0])
        i=1
        while i<len(preorder) and preorder[i]<root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
'''