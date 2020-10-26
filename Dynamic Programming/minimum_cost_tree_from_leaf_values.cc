// Link: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

// Approach: Partition the Array and recursively find minimum cost of each subarray. Now, for current partition
// add min cost of left subtree and right tree along with product of max numbers from both subtree [as indicated 
// in question] and get min of current value with us and calculated value [Line 47]. Store all the computetion in
// an array so that we don't need to recalculate for each recursion. Moreover, also store max_values of each subtree as
// you progress so that we don't need to recalculate it either [Line 46].

class Solution
{
    private:
        int cost[101][101];
        int max_s[101][101];
        
    public: 
        int max(int a, int b)
        {
            return a>b?a:b;
        }
    
        int min(int a, int b)
        {
            return a<b?a:b;
        }
    
        int min_cost(int i, int j, vector<int>& arr)
        {
            if(i == j)
            {
                max_s[i][j] = arr[i];
                return 0;
            }
            
            if((j-i) == 1)
            {
                max_s[i][j] = max(arr[i], arr[j]);
                return arr[i]*arr[j];
            }
            
            if(cost[i][j] == -1)
            {
                int temp = INT_MAX;
                
                for(int k=i;k<j;k++)
                {
                    max_s[i][j] = max(max_s[i][j], arr[k]);
                    temp = min(temp, min_cost(i, k, arr) + min_cost(k+1, j, arr) + max_s[i][k]*max_s[k+1][j]);
                }
                max_s[i][j] = max(max_s[i][j], arr[j]);
                cost[i][j] = temp;
            }
            return cost[i][j];
        }

        int mctFromLeafValues(vector<int>& arr)
        {
            int s = arr.size();
            memset(cost, -1, sizeof(int)*101*101);
            memset(max_s, -1, sizeof(int)*101*101);
            
            return min_cost(0, s-1, arr);
        }
};