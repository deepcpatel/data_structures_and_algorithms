# Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

'''
# Approach:

1). Conventional method is to traverse tree and add elements into dictionary and an array. Now iterate the array and perform conventional 2 Sum. Complexity -> O(2*n).

2). The other O(n) approach is checking whether current node value is in hash set. If it is, then return True, if not, then append (target-node.val) into hash set. This makes anticipation that
    if (target-node.val) is in array/tree in later indices/nodes, then when pointer arrives on that index/node we will check whether that node value is in array, this time it will already be 
    in array thus we return true. Otherwise we return False at last. (Second approach is given below)
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def findTarget(self, root, k):
            queue, el_dict = deque([root]), set()           
            
            while queue:
                node = queue.popleft()
                
                c = k - node.val
                
                if node.val in el_dict:
                    return True
                else:
                    el_dict.add(c)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            return False