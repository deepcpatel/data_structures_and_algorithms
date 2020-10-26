# Link: https://leetcode.com/problems/all-paths-from-source-to-target/

# Approach: Find all possible paths using DFS and Backtracking. Perform DFS on node 0 and set destination as node n-1. When it is encountered in DFS, append the path list into self.paths list.

class Solution(object):
    def dfs(self, node, path_list):
        path_list.append(node)
        
        if node == self.dest:
            self.paths.append(list(path_list))
        else:
            for n in self.graph[node]:
                self.dfs(n, path_list)
                    
        path_list.pop()
            
    def allPathsSourceTarget(self, graph):
        self.paths, self.graph, self.dest = [], graph, len(graph)-1
        self.dfs(0, [])
        return self.paths 
