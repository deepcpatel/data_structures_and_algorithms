// Link: https://leetcode.com/problems/reverse-integer/

class Solution 
{
    public:
        int reverse(int x) 
        {
            long a = 0, tempX = x;
            
            while(tempX != 0)
            {
                a = a*10 + tempX%10;
                tempX = tempX/10;
            }
            
            if(a>INT_MAX || a<-INT_MAX)
            {
                return 0;
            }
            return a;
        }
}; 
