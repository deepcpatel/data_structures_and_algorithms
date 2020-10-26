// Link: https://leetcode.com/problems/generate-parentheses/

class Solution 
{
    private:
        vector<string> answer;
        int sum = 0;
        int lspawned = 0;
        int tot;

    public:
        void recall(string prev, char parent)
        {
            if(parent == '(')
            {
                if(lspawned<tot)
                {
                    lspawned++;
                    sum++;
                    recall(prev+"(", '(');
                    sum--;
                    lspawned--;
                }
                
                if(sum>0)
                {
                    sum--;
                    recall(prev+")", ')');
                    sum++;
                }
            }
            else
            {
                if(sum>0)
                {
                    sum--;
                    recall(prev+")", ')');
                    sum++;
                }
                
                if(lspawned<tot)
                {
                    lspawned++;
                    sum++;
                    recall(prev+"(", '(');
                    sum--;
                    lspawned--;
                }
                
                if(lspawned == tot && sum == 0)
                {
                    answer.push_back(prev);
                }
            }
        }
    
        vector<string> generateParenthesis(int n)
        {
            tot = n;
            
            lspawned++;
            sum++;
            recall("(", '(');
            return answer;
        }
}; 