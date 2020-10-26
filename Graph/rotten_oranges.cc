// Link: https://leetcode.com/problems/rotting-oranges/

// Approach: The general idea is to apply BFS and mark all the healthy oranges near rotten orange as rotten. However, you first have to fill the queue with all the rotten
// oranges (I didn't did at first) because oranges rot in parallel and not the series. So apply BFS simultaneously on rotten oranges. Now, calculate the level of BFS and
// return that. Because it is the time to rot all the oranges (Or max level to traverse all nodes). I have used the variables "c1" and "c2" to calculate levels since I am
// not using recursion. Variable "c1" stores number of parent nodes and "c2" stores number of child nodes. We decrement "c1" as parent node traverses and if it becomes zero,
// we change level (variable named "time" here).

class Solution
{
    private:
        queue<pair<int, int>> node_queue;
        
        void print_grid(vector<vector<int>>& grid)
        {
            int m = grid.size(), n = grid[0].size();
            
            for(int i=0;i<m;i++)
            {
                for(int j=0;j<n;j++)
                {
                    cout<<grid[i][j]<<", ";
                }
                cout<<"\n";
            }
            cout<<"---------------------------------\n";
        }
    
        int bfs(int& one_counter, vector<vector<int>>& grid)
        {
            pair<int, int> p;
            int x = -1, y = -1, m = grid.size(), n = grid[0].size(), time = 0;
            int c1 = node_queue.size(), c2 = 0;
            // node_queue.push(make_pair(i, j));
            
            while(node_queue.size()>0)
            {
                p = node_queue.front();
                x = p.first;
                y = p.second;
                node_queue.pop();
                c1--;
                
                if(x>0)
                {
                    if(grid[x-1][y] == 1)
                    {
                        node_queue.push(make_pair(x-1, y));
                        grid[x-1][y] = -1;
                        one_counter--;
                        c2++;
                    }
                }
                
                if(x<(m-1))
                {
                    if(grid[x+1][y] == 1)
                    {
                        node_queue.push(make_pair(x+1, y));
                        grid[x+1][y] = -1;
                        one_counter--;
                        c2++;
                    }
                }
                
                if(y>0)
                {
                    if(grid[x][y-1] == 1)
                    {
                        node_queue.push(make_pair(x, y-1));
                        grid[x][y-1] = -1;
                        one_counter--;
                        c2++;
                    }
                }
                
                if(y<(n-1))
                {
                    if(grid[x][y+1] == 1)
                    {
                        node_queue.push(make_pair(x, y+1));
                        grid[x][y+1] = -1;
                        one_counter--;
                        c2++;
                    }
                }
                
                if(c1 == 0)
                {
                    c1 = c2;
                    c2 = 0;
                    time++;
                    
                    // print_grid(grid);
                    // cout<<time<<"\n---------\n";
                }
            }
            return --time;
        }
    
    public:
        int orangesRotting(vector<vector<int>>& grid)
        {
            int m = grid.size();
            
            if(m == 0)
            {
                return 0;
            }
            
            int n = grid[0].size(), time = 0, one_counter = 0;
            
            for(int i=0;i<m;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(grid[i][j] == 2)
                    {
                        node_queue.push(make_pair(i, j));
                    }
                    
                    if(grid[i][j] == 1)
                    {
                        one_counter++;
                    }
                }
            }
            
            if(one_counter == 0 && node_queue.size() == 0)
            {
                return 0;
            }
            else
            {
                time = bfs(one_counter, grid);
                
                if(one_counter != 0)
                {
                    return -1;
                }
            }
            return time;
        }
};