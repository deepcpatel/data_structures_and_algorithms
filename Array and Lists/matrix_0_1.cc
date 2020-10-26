// Question: https://leetcode.com/problems/01-matrix
// Using DFS

#include <stack>
#include <utility>
#include <cstdint>

class Solution 
{
    private:
        stack<pair<int, int>> point_stack;  // Stack for the points
        int h;  // Matrix Height
        int w;  // Matrix Width
    
    public:
        // Initializer function
        vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) 
        {
            // Initializing the Vectors and Stacks
            vector<vector<int>> dist_mat(matrix.size(), vector<int>(matrix[0].size()));
            
            h = matrix.size();
            w = matrix[0].size();
            
            // Initializing the values in the Vector
            for(int i=0;i<h;i++)
                for(int j=0;j<w;j++)
                {
                    if(matrix[i][j] != 0)
                    {
                        dist_mat[i][j] = INT_MAX;
                    }
                }
            
            // Iterating over all the elements
            for(int i=0;i<h;i++)
                for(int j=0;j<w;j++)
                {
                    if(matrix[i][j] == 1)
                    {
                        calc_dist(matrix, dist_mat, make_pair(i,j));
                    }
                }
            return dist_mat;
        }
        
        // Display the values in the Vector
        void display_mat(vector<vector<int>>& matrix)
        {
            for(int i=0;i<h;i++)
            {
                for(int j=0;j<w;j++)
                {
                    cout<<matrix[i][j]<<" ";
                }
                cout<<"\n";
            }
        }
    
        // Recursively calculating distance of each node form nearest 0
        int calc_dist(vector<vector<int>>& matrix, vector<vector<int>>& dist_mat, pair<int, int> cord)
        {
            int push_counter = 0;
            pair<int, int> p;
            int min = INT_MAX;
            
            // Marking the current index to prevent it from being visited again
            matrix[cord.first][cord.second] = -1;
            
            // Exploring Neighbours
            if(cord.second-1 >= 0)
            {
                if(matrix[cord.first][cord.second-1] == 0)
                {
                    dist_mat[cord.first][cord.second] = 1;
                    return 1;
                }
                else if(matrix[cord.first][cord.second-1] == 1)
                {
                    point_stack.push(make_pair(cord.first,cord.second-1));
                    push_counter++;
                }
            }
            
            if(cord.second+1 < w)
            {
                if(matrix[cord.first][cord.second+1] == 0)
                {
                    dist_mat[cord.first][cord.second] = 1;
                    return 1;
                }
                else if(matrix[cord.first][cord.second+1] == 1)
                {
                    point_stack.push(make_pair(cord.first,cord.second+1));
                    push_counter++;
                }
            }
            
            if(cord.first-1 >= 0)
            {
                if(matrix[cord.first-1][cord.second] == 0)
                {
                    dist_mat[cord.first][cord.second] = 1;
                    return 1;
                }
                else if(matrix[cord.first-1][cord.second] == 1)
                {
                    point_stack.push(make_pair(cord.first-1,cord.second));
                    push_counter++;
                }
            }
            
            if(cord.first+1 < h)
            {
                if(matrix[cord.first+1][cord.second] == 0)
                {
                    dist_mat[cord.first][cord.second] = 1;
                    return 1;
                }
                else if(matrix[cord.first+1][cord.second] == 1)
                {
                    point_stack.push(make_pair(cord.first+1,cord.second));
                    push_counter++;
                }
            }
            
            // Performing DFS
            for(int i=0;i<push_counter;i++)
            {
                p = point_stack.top();
                point_stack.pop();
                
                calc_dist(matrix, dist_mat, p);
            }
            
            // Finding Minimum distance
            if(cord.second-1 >= 0)
            {
                if(min > dist_mat[cord.first][cord.second-1])
                {
                    min = dist_mat[cord.first][cord.second-1];
                }
            }
            
            if(cord.second+1 < w)
            {
                if(min > dist_mat[cord.first][cord.second+1])
                {
                    min = dist_mat[cord.first][cord.second+1];
                }
            }
            
            if(cord.first-1 >= 0)
            {
                if(min > dist_mat[cord.first-1][cord.second])
                {
                    min = dist_mat[cord.first-1][cord.second];
                }
            }
            
            if(cord.first+1 < h)
            {
                if(min > dist_mat[cord.first+1][cord.second])
                {
                    min = dist_mat[cord.first+1][cord.second];
                }
            }
            
            matrix[cord.first][cord.second] = 1;

            // Changing current distance
            if(min == INT_MAX)
            {
                return INT_MAX;
            }
            else
            {
                dist_mat[cord.first][cord.second] = min+1;
                return min+1;
            }
        }
};
