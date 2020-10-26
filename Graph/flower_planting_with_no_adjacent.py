# Link: https://leetcode.com/problems/flower-planting-with-no-adjacent/

# Approach: Basically, identify current color in the garden and mark that color as used in adjacent gardens, and thus, they will use different colour determined by top_flower() function.
# Each size 4 list represents 4 colours and 1 in each location means colour corrsponding to that index is available. (-1) means not available.

class Solution(object):
    def top_flower(self, flower_list):  # Returns first possible flower colour from list (0, 1, 2, 3)
        if flower_list[0] == 1:
            return 0
        elif flower_list[1] == 1:
            return 1
        elif flower_list[2] == 1:
            return 2
        else:
            return 3
    
    def gardenNoAdj(self, N, paths):
        graph = [[] for i in range(N)]                        # Adjacency list
        flowers = [[1 for j in range(4)] for i in range(N)]   # N elements, 4 Flowers (Available colour indicated by 1 in corresponding location)
        ans_list = [-1]*N   # Stores Answer
        
        # Populating adjacency list
        for p in paths:
            graph[p[0]-1].append(p[1]-1)
            graph[p[1]-1].append(p[0]-1)
            
        # Iterating over each garden
        for i in range(N):
            tf = self.top_flower(flowers[i])    # Identifying possible flower colour for current garden
            ans_list[i] = tf+1                  # Appending into the list
            
            for n in graph[i]:                  # Marking colour tf as used (-1) in adjacent gardens
                flowers[n][tf] = -1
        
        return ans_list