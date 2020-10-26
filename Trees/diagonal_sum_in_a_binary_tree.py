# Link: https://www.geeksforgeeks.org/diagonal-sum-binary-tree/

'''
Consider Red lines of slope -1 passing between nodes (in following diagram). The diagonal sum in a binary tree is the sum of all node’s data lying between these lines. Given a Binary Tree of size N, print all diagonal sums.

For the following input tree, output should be 9, 19, 42.
9 is sum of 1, 3 and 5.
19 is sum of 2, 6, 4 and 7.
42 is sum of 9, 10, 11 and 12.

DiagonalSum

Example 1:

Input:
         4
       /   \
      1     3
           /
          3
Output: 7 4 

Example 2:

Input:
           10
         /    \
        8      2
       / \    /
      3   5  2
Output: 12 15 3 

Your Task:
You don't need to take input. Just complete the function diagonalSum() that takes root node of the tree as parameter and returns an array containing the diagonal sums for every diagonal present in the tree with slope -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=Number of nodes<=105
'''

# Approach: Iterate tree nodes using BFS. Divide the tree in levels. The root node will be at level 0. Now, if you put left child in the queue, it will be in current_level-1 level and right child will
# be in current_level level. Now based on the level, add the current_node.data to the value at corresponding level in dictionary. Finally, iterate all elements in the dictionary starting from 0th level
# and going to min_level and add to a list. Return that final list.

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

def diagonalSum(root):
    queue, sum_dict, min_level, ans = deque([(root, 0)]), {}, 0, []
    
    while queue:
        node, level = queue.popleft()
        sum_dict[level] = sum_dict.get(level, 0) + node.data
        
        if node.left:
            min_level = min(min_level, level-1)
            queue.append((node.left, level-1))
        
        if node.right:
            queue.append((node.right, level))
    
    for i in range(0, min_level-1, -1):
        ans.append(sum_dict[i])
    
    return ans 
