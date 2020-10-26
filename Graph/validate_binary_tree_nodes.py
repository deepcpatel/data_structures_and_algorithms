# Link: https://leetcode.com/problems/validate-binary-tree-nodes/

# Approach: Do BFS in a tree. Goal is to reach all nodes starting from zero with no cycles (cycle means incorrect binary tree). If any node is left from reaching, then it will be new head which 
# created another tree.

from collections import deque
        
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        visit_list, node_q = [0 for i in range(n)], deque([])
        
        for i in range(n):
            if not visit_list[i]:       # Finding new tree root
                node_q.append(i)
                
                while node_q:
                    node = node_q.popleft()      

                    if leftChild[node] != -1:

                        if not visit_list[leftChild[node]]:     # Checking if visited for cycle
                            visit_list[leftChild[node]] = 1     # Marking visited
                        else:
                            return False  

                        node_q.append(leftChild[node])

                    if rightChild[node] != -1:

                        if not visit_list[rightChild[node]]:    # Checking if visited for cycle
                            visit_list[rightChild[node]] = 1    # Marking visited
                        else:
                            return False 

                        node_q.append(rightChild[node])
                
        if sum(visit_list) < n-1:   # Checking if all the nodes are visited extept root (n-1)
            return False
        
        return True