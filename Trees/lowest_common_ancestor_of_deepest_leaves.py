# Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Approach: (Efficient Method - Reffered from discussion) Perform DFS on the tree. At each node, visit left and rught child and obtain the max depth and common ancestor in both the subtrees. After that
# Compare the max depth of both the sides. If both are equal, then return max_deptha and current node (now a new common ancestor). Else if left depth is greater, then return left_depth and left common
# node. Else, finally return right_depth and right common node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self, node, level):
        ldepth, rdepth = level, level
        
        if node.left:
            ldepth, lnode = self.dfs(node.left, level+1)
        
        if node.right:
            rdepth, rnode = self.dfs(node.right, level+1)
            
        if ldepth == rdepth:
            return ldepth, node
        elif ldepth > rdepth:
            return ldepth, lnode
        else:
            return rdepth, rnode
        
    def lcaDeepestLeaves(self, root):
        _, node = self.dfs(root, 1)
        return node

'''
# Approach: Perform DFS and maintain a list of the nodes visited so far. If the node is the leaf node and deeper than current deepest one (determined by 'level' variable), then replace the global visited
# list with the current list. If the node is leaf node and at same deeper level than current one, then compare the global visited list and current visited list. Remove all the elements from global list
# after the last common element. Do it till you traverse whole tree. Remove the last element from the global visited list as final answer.

class Solution(object):
    def dfs(self, node, level, queue):
        if not node.left and not node.right:
            if level > self.max_depth:
                self.max_depth = level
                self.global_queue = list(queue)
            elif level == self.max_depth:
                limit = len(self.global_queue)
                
                for i in range(limit):
                    if self.global_queue[i].val != queue[i].val:
                        for _ in range(limit, i, -1):
                            self.global_queue.pop()
                        break
        
        if node.left:
            queue.append(node.left)
            self.dfs(node.left, level+1, queue)
        
        if node.right:
            queue.append(node.right)
            self.dfs(node.right, level+1, queue)
        
        queue.pop()
                
    def lcaDeepestLeaves(self, root):
        self.global_queue, self.max_depth, queue = [], 0, [root]
        self.dfs(root, 1, queue)
        return self.global_queue[-1]
'''