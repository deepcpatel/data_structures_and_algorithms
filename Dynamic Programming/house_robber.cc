// Link: https://leetcode.com/problems/house-robber/

// Approach: Memoization method (Recursion - Top Down Approach)

class Solution 
{
    public:
    
        int calc_sum(int idx, int* sum, vector<int>& nums)
        {
            int max_sum = 0, s = 0;
            
            if(sum[idx] == -1)
            {
                for(int i=idx+2;i<nums.size();i++)
                {
                    s = calc_sum(i, sum, nums);

                    if(max_sum<s)
                    {
                        max_sum = s;
                    }
                }

                sum[idx] = nums[idx] + max_sum;
            }
            return sum[idx];
        }
    
        int rob(vector<int>& nums) 
        {
            if(nums.size() == 0)
            {
                return 0;
            }
            else if(nums.size() == 1)
            {
                return nums[0];
            }
            
            int sum[nums.size()];
            fill_n(sum, nums.size(), -1);
            
            return max(calc_sum(0, sum, nums), calc_sum(1, sum, nums));
        }
};