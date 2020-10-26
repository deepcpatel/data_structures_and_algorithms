// Link: https://leetcode.com/problems/unique-paths-ii/

class Solution 
{   private:
        vector<vector<int>> array;
 
    public:
        int path(int x, int y, int m, int n)
        {
            if(array[y][x] == -1)
            {
                int count = 0;
                
                if(x+1<m)
                    count += path(x+1, y, m, n);
                if(y+1<n)
                    count += path(x, y+1, m, n);
                array[y][x] = count;
            }
            return array[y][x];
        }
 
        int uniquePathsWithObstacles(vector<vector<int>>& grid)
        {   
            int n = grid.size(), m = grid[0].size();
            
            for(int i=0;i<n;i++)
            {
                array.push_back(vector<int>(m, -1));
            }
            
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<m;j++)
                {
                    if(grid[i][j] == 1)
                    {
                        array[i][j] = 0;
                    }
                }
            }
            
            if(array[n-1][m-1] != 0)
            {
                array[n-1][m-1] = 1;
            }
            return path(0, 0, m, n);
        }
};