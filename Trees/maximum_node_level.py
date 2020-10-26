# Link: https://www.geeksforgeeks.org/level-maximum-number-nodes/

'''
Given a Binary tree. Find the level in binary tree which has the maximum number of nodes.

Example 1:

Input:
      2
    /    \ 
   1      3
 /   \     \
4    6      8
     / 
    5
Output: 2
Explanation: The level 2 with nodes 4,
6 and 8 is the level with maximum
number of nodes. 


Your Task:
You don't need to read input or print anything. Your task is to complete the function maxNodeLevel() that takes root node of the tree as input and returns an integer which is level of the tree with maximum nodes. The root is at level 0. If two or more levels have same number of maximum nodes , then return smallest level.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=Number of level<=10
'''

# Approach: Iterate Tree using BFS. Before popping out nodes from the queue, check the queue size. This will keep track of total nodes at current level. Also pop out those many nodes only from the qieie
# at each iteration. Moreover, keep track of max_nodes and corresponding max_level at each iteration. Finally return max_level

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

def maxNodeLevel(root):
    queue, level, max_len, max_level = deque([root]), 0, -1, -1
    
    while queue:
        qlen = len(queue)
        
        if max_len < qlen:
            max_len, max_level = qlen, level
        
        while qlen:
            
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            qlen -= 1
        
        level += 1
    
    return max_level 