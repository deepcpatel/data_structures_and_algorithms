# Link: https://leetcode.com/problems/course-schedule-ii/

# Approach: Topological Sorting using DFS. Basically this code is similar to Course Schedule except that, while popping from stack, I append that element to the answer list (line 35) and I 
# skip and pop already visited element (line 18).

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adj_list, visited, stack, ans_list, counter = [[] for i in range(numCourses)], [0]*numCourses, [], [-1]*numCourses, numCourses-1
        
        for p in prerequisites:
            adj_list[p[1]].append(p[0])
            
        for i in range(numCourses):
            if visited[i] == 0:
                stack.append(i)
                
                while stack:
                    if visited[stack[-1]] == 1:
                        stack.pop()
                        continue
                        
                    node, app_flag = stack[-1], False
                    visited[node] = -1
                    
                    for n in adj_list[node]:
                        if visited[n] == 1:
                            continue
                        elif visited[n] == -1:
                            return []
                        else:
                            app_flag = True
                            stack.append(n)
                    
                    if app_flag == False:   # No change in stack
                        visited[node], ans_list[counter], counter = 1, stack.pop(), counter - 1
                        
        return ans_list