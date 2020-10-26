# Link: https://leetcode.com/problems/delete-nodes-and-return-forest/

# Approach: Traverse the Tree using DFS. After traversing the left and right child (and updating them with the respective return values), see if current node is in the to_delete list. If it is, 
# then put the left and right child in the tree_node list and return None. Else, return the root as it is. Finally, add the root node in the list it the return value is not None. Finally, return
# the tree node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def dfs(self, node):
        if node.left:
            node.left = self.dfs(node.left)
        
        if node.right:
            node.right = self.dfs(node.right)
            
        if node.val in self.to_delete_set:
            
            if node.left:
                self.tree_nodes.append(node.left)
                
            if node.right:
                self.tree_nodes.append(node.right)
                        
            return None
        
        return node
        
    def delNodes(self, root, to_delete):
        self.tree_nodes, self.to_delete_set = [], set(to_delete)
        ret = self.dfs(root)
        
        if ret:
            self.tree_nodes.append(ret)
        
        return self.tree_nodes