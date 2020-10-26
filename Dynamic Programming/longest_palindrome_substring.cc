// Link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution 
{
    public:
        string longestPalindrome(string s) 
        {
            int start = 0, end = 0, temp, max_len = 0, f_start, f_end;
            
            if(s.compare("") == 0)
            {
                return "";
            }
            
            for(int i=0;i<s.length();i++)
            {
                start = i;
                end = i;
                
                while(s[start] == s[end])
                {
                    temp = end - start + 1;
                    
                    if(max_len < temp)
                    {
                        max_len = temp;
                        f_start = start;
                        f_end = end;
                    }
                    
                    if(--start < 0)
                    {
                        break;
                    }
                    
                    if(++end >= s.length())
                    {
                        break;
                    }
                }
            }
            
            for(int i=0;i<s.length()-1;i++)
            {
                start = i;
                end = i+1;
                
                while(s[start] == s[end])
                {
                    temp = end - start + 1;
                    
                    if(max_len < temp)
                    {
                        max_len = temp;
                        f_start = start;
                        f_end = end;
                    }
                    
                    if(--start < 0)
                    {
                        break;
                    }
                    
                    if(++end >= s.length())
                    {
                        break;
                    }
                }
            }
            return s.substr(f_start, max_len);
        }
}; 
