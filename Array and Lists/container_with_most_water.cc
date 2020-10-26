// Link: https://leetcode.com/problems/container-with-most-water/

class Solution 
{
    public:
        int maxArea(vector<int>& height)
        {
            int max_ar = 0, i = 0, j = height.size()-1, area, h = 0;
            int max_l = 0, max_r = 0, flag = 0;
            
            while(i<j)
            {   
                if(flag == 1)
                {
                    h = (max_l<max_r?max_l:max_r);
                    area = h*(j-i);

                    if(max_ar < area)
                    {
                        max_ar = area;
                    }
                    flag = 0;
                }
                
                if(h<height[i])
                {
                    max_l = height[i];
                    flag = 1;
                }
                else
                {
                    i++;
                }
                
                if(h<height[j])
                {
                    max_r = height[j];
                    flag = 1;
                }
                else
                {
                    j--;
                }
            }
            return max_ar;
        }
};
