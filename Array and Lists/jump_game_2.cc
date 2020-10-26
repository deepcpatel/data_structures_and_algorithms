// Link: https://leetcode.com/problems/jump-game-ii/

// Not my solution
class Solution 
{
    public: 
        int jump(vector<int> &a) 
        {
            int i=0;
            int j=0;
            int b=0;
        
            for(int k=0;k<a.size()-1;k++)
            {
                j=max(j,a[k]+k);
                
                if(k==i)
                {
                    b++;
                    i=j;
                    
                    if(i>=a.size()-1)
                    {
                        break;
                    }
                }
            }
            return b;
        }
}; 
