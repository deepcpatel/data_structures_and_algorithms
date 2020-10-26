# Link: https://practice.geeksforgeeks.org/problems/remove-half-nodes/1

'''
Given A binary Tree. Your task is to remove all the half nodes (which has only one child).

Example 1:

Input:
         7
       /   \
      7     8
     / 
    2
Output: 2 7 8 

Example 2:

Input:
         2
       /   \
      7     5
       \      \
        9      1
       /  \
      11   4
Output: 1 6 11 2 4

Your Task:
You don't need to read input or print anything. Your task is to complete the function removeHalfNodes() which takes the root node of the tree as input and returns the root node of the modified tree after removing all the half nodes, ie the ones having just a single child node. (The inorder traversal of the returned tree is printed by the driver's code.)
For example consider the below tree.

Nodes 7, 5 and 9 are half nodes as one of their child is Null. We need to remove all such half nodes and return the root pointer of following new tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Binary Tree).

Constraints:
1<=Number of nodes<=104
'''

# Approach: Recursively visit each Node in the Tree. If that node has no children, then return the node itself as it is not half node. If that node has 2 children then update its left and right
# children by calling RemoveHalfNodes() on them and return the node. If the node has either one children, then we want to remove theat node, thus we will not return it, instead we will return either
# its left children or right child haveing RemoveHalfNodes() called on them (Line 54 and 56).

def RemoveHalfNodes(root): 
    if not root:
        return None
    
    if (root.left and root.right) or not (root.left or root.right):
        root.left = RemoveHalfNodes(root.left)
        root.right = RemoveHalfNodes(root.right)
        return root
    elif root.left and not root.right:
        return RemoveHalfNodes(root.left)
    elif root.right and not root.left:
        return RemoveHalfNodes(root.right)