'''
Link: https://practice.geeksforgeeks.org/problems/full-binary-tree/1/?track=amazon-trees&batchId=192

Given a Binary Tree. Check whether the Binary tree is a full binary tree or not.

Example 1:

Input:
          1
       /    \
      2      3
    /   \
   4     5
Output: 1
Explanation: Every node except leaf node
has two children so it is a full tree.

Example 2:

Input:
          1
       /    \
      2      3
    /   
   4     
Output: 0
Explanation: Node 2 has only one child
so this is not a full tree.

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function isFullTree() which takes the root node of the tree as input and returns True if the given Binary Tree is full. Else, it returns False. (The driver code will print 1 if the returned value is true, otherwise 0).

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1<=Number of nodes<=1000
'''

# Approach: Use BFS to iterate every node in Tree. Now for each node, check whether it has 0 or 2 nodes. If only one node is there then return False. Else Finally return True

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
        
# Return True if the given Binary Tree is a Full Binary Tree. Else return False
def isFullTree(root):
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if not (node.left or node.right):
            continue
        elif (node.left and node.right):
            queue.extend([node.left, node.right])
        else:
            return False
    
    return True