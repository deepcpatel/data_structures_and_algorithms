# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Approach: First of all make a dictionary which stores each element in inorder list and its corresponding position in that. Now, our approach will be to start iterating each element in preorder
# from 0th index. The first element of preorder will be tree, as in preorder traversal, we first print the current node and them move to its children. Make TreeNode of each element in the preorder
# array and store it in the stack. Along with TreeNode, also store its current position and end index of its inorder array span. The end index of an element's Array span is decided as follows:
# 
# Let, inorder = [3 1 4 0 5 2] and preorder=[0 1 3 4 2 5], n = len(inorder) == 6 here. Now, we start with 0th index in preorder, which is 0 value and is root of tree. In inorder it is at 3rd index.
# In the stack we store(TreeNode(0), 3, 6-1). Here 6-1 = 5 is last index of array spanned by 0. 
# 
# Now, in the above example, according to the algorithm, we will start loop from 1 to n in preorder. We will encounter 1. Its index in inorder is 1. Now, since 1 is smaller than 3 (index of 0), we will
# make 1 the left sub child of 0 and store (TreeNode(1), 1 -> inorder idx, 3). Now, since 1 is left child of 0, its array span will be left inorder sub array (left to 0) and thus its end index will be 3, 
# which we store in stack. Next comes 3 in preorder. 3's index in inorder is 0. Since 0 is in the span of 1 (0 < 3) [Here 1 is top element of stack], 3 could be one of children of 1. Since inorder_idx of 
# 3 is < smaller than that of 1 (stack[-1][1]), we make three the left child of 1 and store in stack (TreeNode(3), 0, 1). Array span of 3 is left inorder array of 1 and thus its end index is 1. Now, we move
# to 4 in preorder. Its inorder_idx is 2. since 2 is greater than stack[-1][2] (4 is not in span array of 3, thus it is not its child), thus pop 3 from stack. Now, 4 is in span array of stack[-1] (here 1),
# and since 2 is greater than 1, make 4 the right child of 1 and store in stack (TreeNode(4), 2, 3). Here 3 is end index of right inorder array span, since 4 is right of 1 and left og 0 in order. Continue
# this till you reach to end of pre order. Now return stack[0][0], which is root node of the tree. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        n = len(inorder)
        if n == 0:
            return None
        
        el_position = {inorder[i]:i for i in range(n)}
        stack = [(TreeNode(val=preorder[0]), el_position[preorder[0]], n-1)]    # Root Node
        
        for i in range(1, n):
            inorder_pos, curr_node = el_position[preorder[i]], TreeNode(val=preorder[i])

            while inorder_pos > stack[-1][2]:
                stack.pop()

            if inorder_pos > stack[-1][1]:
                stack[-1][0].right = curr_node
                stack.append((curr_node, inorder_pos, stack[-1][2]))
            else:
                stack[-1][0].left = curr_node
                stack.append((curr_node, inorder_pos, stack[-1][1]))
                
        return stack[0][0]  # Returning Root Node