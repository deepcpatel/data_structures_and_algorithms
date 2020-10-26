# Link: https://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/

'''
Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums through different vertical lines starting from left-most vertical line to right-most vertical line.

Example 1:

Input:
       1
    /   \
  2      3
 / \    / \
4   5  6   7
Output: 
Explanation:
The tree has 5 vertical lines
Vertical-Line-1 has only one node
4 => vertical sum is 4
Vertical-Line-2: has only one node
2=> vertical sum is 2
Vertical-Line-3: has three nodes:
1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3
=> vertical sum is 3
Vertical-Line-5: has only one node 7
=> vertical sum is 7

Your Task:
You don't need to take input. Just complete the function verticalSum() that takes root node of the tree as parameter and returns an array containing the vertical sum of tree from left to right.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=Number of nodes<=1000
'''

# Approach: Label vertical partitions using numbers. Then our root node would start from zero. When you visit to left child decrease current level with -1 and similarly for right child, increase current
# level to 1. Now, maintain a dictionary that stores sums for all levels. Traverse the nodes using BFS. At every nodel, keep track of its level and after visiting it, add its value into dictionary
# at corresponding level. Maintain, max and min level. Finally after BFS, iterate the dictionary keys through min to max and store each sum into an array. Finally return that array.

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

# Complete the function below
def verticalSum(root):
    node_dict, queue, ans = {}, deque([(root, 0)]), []
    min_range, max_range = 0, 0
    
    while queue:
        node, slot = queue.popleft()    # Each pop will give us node and its vertical level (slot)
        node_dict[slot] = node_dict.get(slot, 0) + node.data
        
        if node.left:
            queue.append((node.left, slot-1))   # We put each left child node and its vertical level (slot-1) into queue for visiting
            min_range = min(min_range, slot-1)  # Determines label of left most level
        
        if node.right:
            queue.append((node.right, slot+1))  # We put each right child node and its vertical level (slot+1) into queue for visiting
            max_range = max(max_range, slot+1)  # Determines label of right most level
    
    for i in range(min_range, max_range+1):
        ans.append(node_dict[i])
    
    return ans 
