# Link: https://practice.geeksforgeeks.org/problems/check-if-two-nodes-are-cousins/1/?

# Approach: Traverse the Tree using BFS. At each level, Check whether a and b are present or not. If both of them are present and have different parent then they are cousing. If only one of them
# is present then they are not cousins, thus return False. If none of them is present, then wait for them to be found.

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

from collections import deque

# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
def isCousin(root, a, b):
    queue = deque([(root, -1)])
    par_a, par_b = None, None
    
    while queue:
        qlen = len(queue)
        
        while qlen:     # Separating levels
            node, parent = queue.popleft()
            
            if node.data == a:
                par_a = parent
            
            if node.data == b:
                par_b = parent
            
            if node.left:
                queue.append((node.left, node.data))
            
            if node.right:
                queue.append((node.right, node.data))
            
            qlen -= 1
            
        if not (par_a or par_b):    # None of the node is in this level
            continue
        elif par_a and par_b:       # Both of the Node is in this level
            if par_a != par_b:      # Their parents are different
                return True
            else:                   # Their parents is same
                return False        
        else:                       # Only one of either nodes is in this level (not other)
            return False