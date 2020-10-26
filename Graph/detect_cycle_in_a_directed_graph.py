# Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1/

# Approach: Use DFS to Keep track of cycles. Mark visited nodes as -1, unvisited as 0 and in progress nodes as 1. During DFS, if you encounter In progress nodes, then it is cycle. Else, after completing
# DFS for a node, mark that as completed. 

def isCyclic(n, graph):
    stack, status = [], [0]*n   # 0 -> Unvisited, 1 -> In progress, -1 -> Visited
    
    for i in range(n):
        if status[i] == 0:  # Unvisited
            stack.append(i)
            
            while stack:
                top, beg_size = stack[-1], len(stack)
                status[top] = 1    # In progress
                
                for n in graph[top]:
                    if status[n] == 0:
                        stack.append(n)
                    elif status[n] == 1:
                        return True
                
                if beg_size == len(stack):
                    status[top] = -1   # Visited the Node
                    stack.pop()
    return False