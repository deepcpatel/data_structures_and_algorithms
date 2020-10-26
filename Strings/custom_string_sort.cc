// Link: https://leetcode.com/problems/custom-sort-string/

// My solution is inspired from somebody else's
class Solution 
{
    public:
        string customSortString(string S, string T)
        {
            string ans = "", rem = "";
            
            for(int i=0;i<S.length();i++)
            {
                for(int j=0;j<T.length();j++)
                {
                    if(S[i] == T[j])
                    {
                        ans += T[j];
                    }
                    else
                    {
                        rem += T[j];    
                    }
                }
                T = rem;
                rem = "";
            }
            return ans + T;
        }
};
