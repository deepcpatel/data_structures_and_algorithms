// Link: https://leetcode.com/problems/two-sum/

class Solution 
{
    public:
        vector<int> twoSum(vector<int>& nums, int target) 
        {
            map<int, int> values;
            map<int,int>::iterator it;
            vector<int> ans;
            
            int temp;
            
            for(int i=0;i<nums.size();i++)
            {
                values.insert(make_pair(nums[i], i));
            }
            
            for(int i=0;i<nums.size();i++)
            {
                temp = target - nums[i];
                
                it = values.find(temp);
                if(it != values.end())
                {
                    if(values[temp] != i)
                    {
                        if(values[temp]>i)
                        {
                            ans.push_back(i);
                            ans.push_back(values[temp]);
                            return ans;
                        }
                        else
                        {
                            ans.push_back(values[temp]);
                            ans.push_back(i);
                            return ans;
                        }
                    }
                }
            }
            return ans;
        }
}; 
