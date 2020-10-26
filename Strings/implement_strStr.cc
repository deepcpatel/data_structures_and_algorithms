// Link: https://leetcode.com/problems/implement-strstr/

// Approach: Brute force Method

class Solution
{
    public:
        int strStr(string haystack, string needle)
        {
            int start = 0, j = 0, len = needle.length();
            
            if(len == 0)
            {
                return 0;
            }
            
            for(int i=0;i<haystack.length();i++)
            {
                if(haystack[i] == needle[j])
                {   
                    if(j == 0)
                    {
                        start = i;       
                    }
                    
                    j++;
                    
                    if(j == len)
                    {
                        return start;   
                    }
                }
                else
                {
                    if(j != 0)
                    {
                        j = 0;
                        i = start;
                    }
                }
            }
            return -1;
        }
}; 
