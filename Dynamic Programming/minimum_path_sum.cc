// Link: https://leetcode.com/problems/minimum-path-sum/

class Solution
{   private:
        vector<vector<int>> score;
    public:
        int calc_score(int x, int y, int m, int n, vector<vector<int>>& array)
        {
            if(score[x][y] == -1)
            {
                int c1 = INT_MAX, c2 = INT_MAX;
                
                if(x+1<m)
                    c1 = calc_score(x+1, y, m, n, array);
                
                if(y+1<n)
                    c2 = calc_score(x, y+1, m, n, array);
                
                if(c1<c2)
                    score[x][y] = array[x][y] + c1;
                else if(c2<c1)
                    score[x][y] = array[x][y] + c2;
                else
                {
                    if(c1 == INT_MAX && c2 == INT_MAX)
                    {
                        score[x][y] = array[x][y];
                    }
                    else
                    {
                        score[x][y] = array[x][y] + c1;
                    }
                }
            }
            return score[x][y];
        }
 
        int minPathSum(vector<vector<int>>& grid)
        {
            int m = grid.size(), n = grid[0].size();
            
            for(int i=0;i<m;i++)
            {
                score.push_back(vector<int>(n, -1));
            }
            return calc_score(0, 0, m, n, grid);
        }
}; 
