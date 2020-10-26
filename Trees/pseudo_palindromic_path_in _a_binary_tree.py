# Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Approach: Traverse the tree using DFS. Keep track of elements in the path by adding it in a set (or removing if already there to mark a pair for palindrome). After reaching at leaf node, check whether
# the set is empty or have one element. If true then the path is pseudo palindromic, increment the counter. Before exiting the node, revert the set into same state as beginning (ie, if you removed
# element in the beginning, then add it back, or if you added the element in the beginning, then remove it).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, num_set):
        
        # Doing (Removing value if it exist, else add the current value if does not exist)
        if node.val in num_set:
            num_set.remove(node.val)
        else:
            num_set.add(node.val)
        
        if not node.left and not node.right:   # If set is empty or have only one element, it means that all the duplicate elements capable of forming palindrome are detected (or there were no duplicate elements at all)
            if len(num_set) <= 1:
                self.palindrome_counter += 1
        
        if node.left:
            self.dfs(node.left, num_set)
        
        if node.right:
            self.dfs(node.right, num_set)
        
        # Undoing (Making the set in the same state as in beginning, before leaving this node)
        if node.val in num_set:
            num_set.remove(node.val)
        else:
            num_set.add(node.val)
                  
    def pseudoPalindromicPaths (self, root):
        self.palindrome_counter = 0
        self.dfs(root, set())
        
        return self.palindrome_counter