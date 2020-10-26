// Link: https://leetcode.com/problems/3sum/

// Not my Solution

class Solution 
{
    public:
        vector<vector<int>> threeSum(vector<int>& nums) 
        {
            sort(nums.begin(), nums.end());
            vector<vector<int>> res;
            if (nums.size() < 3) return res;
            for (int i = 0; i < nums.size() - 2; i++) 
            {
                int beg = i + 1, end = nums.size() - 1, tmp = -1 * nums[i];

                if (i > 0 && nums[i] == nums[i - 1]) continue;
                while (beg < end) 
                {
                    if (tmp == nums[beg] + nums[end]) 
                    {
                        res.push_back(vector<int>({nums[i], nums[beg], nums[end]}));
                        while (beg < end && nums[beg] == nums[beg + 1]) beg++;
                        while (beg < end && nums[end] == nums[end - 1]) end--;
                        beg++;
                        end--;
                    }
                    else if (tmp < nums[beg] + nums[end]) end--;
                    else beg++;
                }
            }
            return res;
        }
};