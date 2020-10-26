// Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution 
{
    public:
        int lengthOfLongestSubstring(string s)
        {
            int max_len = 0, start = 0, end = 0, len = 0;
            char ch = 'a';
            map<char, int> alpha;
            
            if(s ==  " ")
            {
                return 1;
            }
            
            for(int i=0;i<26;i++)
            {
                alpha.insert(make_pair(ch, 0));
                ch = (char)((int)ch + 1);
            }
            
            while(start<s.length() && end<s.length())
            {
                if(alpha[s[end]] > 0)
                {
                    while(alpha[s[end]] > 0)
                    {
                        alpha[s[start]] -= 1;
                        start++;
                    }
                    len = end - start;
                }
                else
                {
                    alpha[s[end]] += 1;
                    end++;
                    len++;
                    
                    if(max_len < len)
                    {
                        max_len = len;
                    }
                }
            }
            return max_len;
        }
};
