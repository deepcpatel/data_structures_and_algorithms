// Link: https://leetcode.com/problems/number-of-islands/
// Approach: Perform BFS starting from a node of value 1. Mark all connected nodes as visited, so that you do not visit them again.
//           Increment the counter as you encounter unvisited 1 (in numIslands function).

#include <queue>

class Solution
{
    private:
        queue<pair<int, int>> node_queue;
        
        void bfs(int i, int j, vector<vector<char>>& grid)
        {
            pair<int, int> p;
            int x = -1, y = -1, m = grid.size(), n = grid[0].size();
            node_queue.push(make_pair(i, j));
            
            while(node_queue.size()>0)
            {
                p = node_queue.front();
                x = p.first;
                y = p.second;
                node_queue.pop();
                
                if(x>0)
                {
                    if(grid[x-1][y] == '1')
                    {
                        node_queue.push(make_pair(x-1, y));
                        grid[x-1][y] = '-';
                    }
                }
                
                if(x<(m-1))
                {
                    if(grid[x+1][y] == '1')
                    {
                        node_queue.push(make_pair(x+1, y));
                        grid[x+1][y] = '-';
                    }
                }
                
                if(y>0)
                {
                    if(grid[x][y-1] == '1')
                    {
                        node_queue.push(make_pair(x, y-1));
                        grid[x][y-1] = '-';
                    }
                }
                
                if(y<(n-1))
                {
                    if(grid[x][y+1] == '1')
                    {
                        node_queue.push(make_pair(x, y+1));
                        grid[x][y+1] = '-';
                    }
                }
            }
        }
    
    public:
        int numIslands(vector<vector<char>>& grid)
        {
            int m = grid.size();
            
            if(m == 0)
            {
                return 0;
            }
            
            int n = grid[0].size(), counter = 0;
            
            for(int i=0;i<m;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(grid[i][j] == '1')
                    {
                        counter++;
                        bfs(i, j, grid);
                    }
                }
            }
            return counter;
        }
};