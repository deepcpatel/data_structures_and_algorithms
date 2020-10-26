# Link: https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1/

# Approach: Traverse tree using binary search. When popping node from queue, if leve even, then add that element from back in a temp list. If it is odd, then add from front. After every level traversal
# Add temp list to the ans list. Finally return ans list.


def zigZagTraversal(root):
    ans, level, queue, temp = [], 0, deque([root]), []
    
    while queue:
        qlen, temp = len(queue), deque()
        
        while qlen:
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
                    
            if node.right:
                queue.append(node.right)
                
            if level%2 == 0:
                temp.append(node.data)
            else:
                temp.appendleft(node.data)
        
            qlen -= 1
        
        ans.extend(temp)
        
        level += 1
    
    return ans