# Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Approach: You have to do inorder traversal of the tree which is nothing but sorting the tree elements in increasing order. Initialize two variables element and count
# to keep track the previous element in hand and number of its counts. Now at every level, in inorder traversal check if element is same as current node value. If not
# then we have to reset the counter to 0. Now increment the counter and assign element to be current node value. Additionally, we will initialize a list to store
# final answer. After every counter increment, we store co=urrent count value and current element in the list in the form of tuple. Thus at the current node also, adter
# incrementing the counter we check whether it is greater tha last element in the list. If it is, then empty the list and enter the enter the current element and its counter
# If it is equal then do not empty the list, just simply append the current element and its count, else do nothing. Finally return the elements from the ans_list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorder(self, node):     
        if node.left:
            self.inorder(node.left)
        
        if self.element == float('inf') or self.element != node.val:
            self.count = 0
        self.element, self.count = node.val, self.count+1
        
        if self.count > self.ans_li[-1][0]:
            while self.ans_li:
                self.ans_li.pop()
            self.ans_li.append((self.count, self.element))
        elif self.count == self.ans_li[-1][0]:
            self.ans_li.append((self.count, self.element))
            
        if node.right:
            self.inorder(node.right)
        
    def findMode(self, root):
        if not root:
            return []
        
        self.ans_li, self.element, self.count = [(0, float('-inf'))], float('inf'), 0
        self.inorder(root)
        _, nums = zip(*self.ans_li)
        
        return nums