# Link: https://practice.geeksforgeeks.org/problems/height-of-spiral-tree/1/
# Link: https://www.geeksforgeeks.org/find-height-of-a-special-binary-tree-whose-leaf-nodes-are-connected/

'''
Given a special Binary Tree whose leaf nodes are connected to form a circular doubly linked list. Find the height of this special Binary Tree.

Example 1:

Input:
        1
      /   \
     2     3
    /
   4
Output: 3
Explanation: There are 3 edges and 4
nodes in spiral tree where leaf nodes
4 and 3 are connected in circular
doubly linked list form. Thus the
height of spiral tree is 3.

Example 2:

Input:
        1
      /   \
     2     3
    / \
   4   5
  /
 6
Output: 4

Your Task:
You don't need to read input or print anything. Your task is to complete the function findTreeHeight() which takes the root of the special Binary Tree as its input and returns the Height of this special Binary Tree.
In a special Binary Tree, the leaf nodes form a circular doubly linked list.
For Example:

      1
     /   \ 
    2    3
   /  \
  4  5
 /  
6 

In the above binary tree, 6, 5 and 3 are leaf nodes and they form a circular doubly linked list. Here, the left pointer of leaf node will act as a previous pointer of circular doubly linked list and its right pointer will act as next pointer of circular doubly linked list.

Expected Time Complexity: O(Height of the Tree).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 104
'''

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Approach: Traverse the Tree using BFS. At each iteration, determine length of queue (let it be qlen) and pop the nodes and push their child until qlen == 0. Then, increment the height (it means
# that one tree level is completed). Now again do the same steps until queue is empty. We should not pish the child of Leaf nodes into the queue as they are not actual chils, they are nearest leaf nodes.
# Doing so, would have infinite loop. Thus, we determine a node is leaf node is node == node.left.right or node == node.right.leaf (which means that it is a part of doubly linked list). Thus we continue
# our loop if the current node is leaf node.

from collections import deque

# Return the height of the given special binary tree
def findTreeHeight(root):
    queue, level = deque([root]), 0
    
    while queue:
        qlen = len(queue)
        
        while qlen:
            node = queue.popleft()
            
            if node.left and (node != node.left.right):
                queue.append(node.left)
            
            if node.right and (node != node.right.left):
                queue.append(node.right)
                    
            qlen -= 1
            
        level += 1
    
    return level