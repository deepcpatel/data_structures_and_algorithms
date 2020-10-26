# Link: https://leetcode.com/problems/course-schedule-iv/

# Approach: Make adjacency list from the prerequisites list. Now iterate the graph using DFS. Make a parent table of shape (nxn). Each row represent a node from 0 to n-1 and self.parent[i][j] == 1 means
# Node i is parent of j. Or j is children of i. Now as you explore nodes using DFS, Copy values of self.parent[j] to self.parent[i] for each children j of node i. This indicates that children of 
# node j is also children of node i.

class Solution(object):
    
    def dfs(self, i, n):
        
        for j in self.nodes[i]:
            if self.visited[j] == 1:
                for k in range(n):
                    self.parent[i][k] = self.parent[i][k] or self.parent[j][k]
                self.parent[i][j] = 1
            else:
                self.visited[j] = 1
                self.dfs(j, n)
                
                for k in range(n):
                    self.parent[i][k] = self.parent[i][k] or self.parent[j][k]
                self.parent[i][j] = 1
    
    def checkIfPrerequisite(self, n, prerequisites, queries):
        self.parent, self.nodes, self.visited = [[0]*n for i in range(n)], [[] for i in range(n)], [0 for i in range(n)]
        ans_list = []
        
        for p in prerequisites:
            self.nodes[p[0]].append(p[1])
        
        for i in range(n):
            if self.visited[i] == 0:
                self.visited[i] = 1
                self.dfs(i, n)
        
        for q in queries:
            if self.parent[q[0]][q[1]] == 1:
                ans_list.append(True)
            else:
                ans_list.append(False)
        
        return ans_list

'''
# Faster version
# Modifications: Instead of matrices as above, I am using binary numbers to store children. For example, If i want to store j as children for node i, then I do self.parent[i] |= (1<<j). This will
# copy 1 to jth place in ith node. If I want to check the presence of 1 in jth position, I do "if self.parent[i & (1<<j))>>j == 1".

class Solution(object):
    
    def dfs(self, i, n):
        self.parent[i] |= 1<<i  # Making i parent of i
        
        for j in self.nodes[i]:
            if self.parent[j] == 0:             # j has no children, then go to DFS
                self.dfs(j, n)
                
            self.parent[i] |= self.parent[j]    # Copying children of j to i
    
    def checkIfPrerequisite(self, n, prerequisites, queries):
        self.parent, self.nodes = [0 for i in range(n)], [[] for i in range(n)]
        
        for p in prerequisites:
            self.nodes[p[0]].append(p[1])
        
        for i in range(n):
            if self.parent[i] == 0:
                self.dfs(i, n)
        
        return [True if (self.parent[q[0]] & (1<<q[1]))>>q[1] else False for q in queries]  # Checking whether there is child using and operation
'''