// Link: https://leetcode.com/problems/palindrome-number/

class Solution 
{
    public:
        bool isPalindrome(int x) 
        {
            if(x<0)
            {
                return false;
            }
            
            long temp = x, num = 0;
            
            while(temp!=0)
            {
                num = num*10 + temp%10;
                temp = temp/10;
            }
            
            if(x - num == 0)
            {
                return true;
            }
            return false;
        }
};