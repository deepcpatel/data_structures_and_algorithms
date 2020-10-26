// Link: https://leetcode.com/problems/remove-element/

class Solution
{
    public:
        int removeElement(vector<int>& nums, int val)
        {
            int counter = 0;
            for(int i=0;i<nums.size();i++)
            {
                if(nums[i] == val)
                {
                    continue;
                }
                nums[counter] = nums[i];
                counter++;
            }
            return counter;
        }
}; 
