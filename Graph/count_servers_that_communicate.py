# Link: https://leetcode.com/problems/count-servers-that-communicate/

# Approach: Iterate through all cells with value 1 and at same time for each corresponding row number and column number add 1 to row_count and column_count respectively. These ith or jth cell in 
# row_count or column_count arrays indicate number of ones in ith row or jth column of grid. When iterating grid, also count total number of ones encountered (for 1st column having one in each row) 
# and save those indices to a list (as in line 20). In next loop, again visit coordinates with value 1 (lin 19) and subtract those from count whose ith row and jth column has no other one (apart 
# from current one) [line 22 and 23].

# Efficient Solution
class Solution(object):
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])    # Num of Columns            
        row_count, column_count, xy_dict, counter = [0]*m, [0]*n, {}, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i], column_count[j], counter = row_count[i] + 1, column_count[j] + 1, counter + 1
                    
                    if i not in xy_dict:
                        xy_dict[i] = j

        for i in xy_dict:
            if row_count[i] == 1 and column_count[xy_dict[i]] == 1:
                counter -= 1

        return counter

'''
# Approach: Visit each node equal to value 1 and count 1s along row and column of it and mark them -1 (visited). Add both the counts to final answer. Now when counting rows and columns if you encounter -1
# then just add one to final count as -1s means they are already added to counter, thus we will add 1 for current node[i][j].

# Brute Force
class Solution(object):
    def countServers(self, grid):
        m = len(grid)   # Num of rows
        
        if m>0:
            n = len(grid[0])    # Num of Columns
            counter, flag = 0, False
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        
                        for k in range(m):
                            if grid[k][j] == 1:
                                grid[k][j], counter, flag = -1, counter+1, True
                            elif grid[k][j] == -1:
                                flag = True
                                
                        for k in range(n):
                            if grid[i][k] == 1:
                                grid[i][k], counter, flag = -1, counter+1, True
                            elif grid[i][k] == -1:
                                flag = True
                        
                        if flag == True:
                            counter += 1
                            flag = False
                            
                        grid[i][j] = -1
            return counter
        else:
            return 0
'''