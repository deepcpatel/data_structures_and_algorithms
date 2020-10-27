# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Approach: Construct a dictionary from post_order traversal where key is element and value is its position in post_order. Make a stack and append all the values from inorder. If new elements's position
# in postorder that that of top element in stack, then remove top element. Continue this till this condition fails. After that, make the current node either left or right child of new top stack element
# depending on whichever position is open (prefer left first) and append current element in stack. Finally return node at 0th position in stack.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def constructFromPrePost(self, pre, post):
        pos_dict, stack = {post[i]:i for i in range(len(post))}, []
        
        for i in pre:
            node = TreeNode(val=i)
            
            if not stack:
                stack.append(node)
            else:
                while pos_dict[i] > pos_dict[stack[-1].val]:
                    stack.pop()
                
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                
                stack.append(node)
        
        return stack[0]