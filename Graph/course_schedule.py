# Link: https://leetcode.com/problems/course-schedule/

# Approach: Basically, use DFS to detect any cycles in graph. If both the courses are prerequisite of each other, then it forms a cycle and thus they cannot be completed.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        node_dict, visited, stack = [[] for i in range(numCourses)], [0]*numCourses, []
        
        # Making Adjacency list
        for p in prerequisites:
            node_dict[p[1]].append(p[0])   
        
        # Detecting cycle using DFS
        for i in range(numCourses):
            if visited[i] == 0:
                stack.append(i)     # Add into stack for visit
                
                while stack:        # Iterating neighbours
                    node, append_flag = stack[-1], False
                    visited[node] = -1                  # Marking node as "touched"
                    
                    for neighbour in node_dict[node]:
                        if visited[neighbour] == 1:     # If neighbour node is already "finished" then ignore it
                            continue
                        elif visited[neighbour] == -1:  # If neighbour node is already "touched" then it is cycle. Return False
                            return False
                        else:                           # If neighbour node is not "finished" before, then add it in our visit list
                            append_flag = True          # Mark "True" if the current node have "neighbours"
                            stack.append(neighbour)     
                            
                    if append_flag == False:            # Remove the current node if it does not have any neighbour node
                        visited[stack.pop()] = 1        # Node is visited and already "finished" with
        
        return True # Return True if cycle i not found