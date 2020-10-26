# Link: https://leetcode.com/problems/all-possible-full-binary-trees/

# Approach: For each level, recursively call get_tree() function to form left and right sub trees for a current Node. Each get_tree() call would get Number of nodes remining (N) as an argument and
# it has to form the sub trees with those remining number of nodes To get all the combinations of trees, run a for loop by varying number of nodes assigned to form left sub tree (i) and number
# of nodes assigned to right sub trees(N-1-i) [Here, 1 is subtracted to form the current node]. Return those sub trees and form the bigger tree. To save the computation, save those sub trees list in
# a dictionary, so that they can be returned back without calculation (Memoization).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def get_tree(self, N):
        if N not in self.tree_dict:
            li = []
            
            if N == 1:
                li.append(TreeNode(val=0))
            else:
                for i in range(1, N-1, 2):
                    for left_tree in self.get_tree(i):
                        for right_tree in self.get_tree(N-1-i):
                            li.append(TreeNode(val=0, left=left_tree, right=right_tree))
            
            self.tree_dict[N] = li
            
        return self.tree_dict[N]
               
    def allPossibleFBT(self, N):
        self.tree_dict = {}
        return self.get_tree(N)