// Link: https://leetcode.com/problems/climbing-stairs/

class Solution
{
    public:
        int climbs(int pos, vector<int>& scores)
        {
            if(scores[pos] == -1)
            {
                int counter = 0, n = scores.size();
                
                if(pos+1 == n)
                {
                    counter += 1;
                }
                else 
                {
                    if(pos+1<n)
                    {
                        counter += climbs(pos+1, scores); 
                    }

                    if(pos+2<n)
                    {
                        counter += climbs(pos+2, scores); 
                    }
                }
                
                scores[pos] = counter;
            }
            return scores[pos];
        }
    
        int climbStairs(int n)
        {
            if (n == 1 || n == 2)
            {
                return n;
            }
            
            vector<int> scores(n,-1);
            climbs(0, scores);
            
            /*
            for(int i=0;i<scores.size();i++)
            {
                cout<<scores[i]<<"\n";
            }
            */
            
            return scores[0]+scores[1];
        }
}; 
