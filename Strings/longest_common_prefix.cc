// Link: https://leetcode.com/problems/longest-common-prefix/

class Solution 
{
    public:
        string longestCommonPrefix(vector<string>& strs)
        {
            int size = strs.size(), temp = 0, min_len = INT_MAX;;
            string min_str="";
            
            if(!strs.size())
                return min_str;

            for(int i=0;i<size;i++)
            {
                if(min_len>strs[i].length())
                {
                    min_len = strs[i].length();
                    min_str = strs[i];
                }
            }

            for(int i=0;i<size;i++)
            {
                temp = 0;
                for(int j=0;j<min_len;j++)
                {
                    if(min_str[j] != strs[i][j])
                    {
                        break;
                    }
                    temp++;
                }

                min_len = temp;

                if(temp == 0)
                {
                    break;
                }
            }
            return min_str.substr(0, min_len);
        }
}; 
