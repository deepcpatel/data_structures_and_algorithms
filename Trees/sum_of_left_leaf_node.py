# Link: https://practice.geeksforgeeks.org/problems/sum-of-left-leaf-nodes/1/

# Approach: Traverse tree using BFS. Before inserting the child into the queue, also, insert which child it is (left - 1 or right - 0). When popping, add the value of left leaf node in the sums
# variable. Later return the sums

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''

from collections import deque
    
def leftLeavesSum(root_node):
    queue, sums = deque([(root_node, 0)]), 0
    
    while queue:
        node, orientation = queue.popleft()
        
        if node.left:
            queue.append((node.left, 1))
        
        if node.right:
            queue.append((node.right, 0))
        
        if not (node.left or node.right) and orientation == 1:
            sums += node.data
    
    return sums