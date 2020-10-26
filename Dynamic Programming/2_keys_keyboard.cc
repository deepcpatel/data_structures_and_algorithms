// Link: https://leetcode.com/problems/2-keys-keyboard/

// Not my solution

class Solution
{
    public:    
        int count(int current, int cache, int n)
        {
            // Cache stores number of A in previous copy
            // Current stores current number of A
            
            if(current>n)
            {
                return 100000000;   // Current sequence length is exceeding the given limit, return Max Number
            }
            else if(current == n)
            {
                return 0;           // Condition already statisfied, no need of further operations
            }
            else
            {
                int c = 2 + count(2*current, current, n);   // Copy + Paste Operation (Recursive)
                int p = INT_MAX;                            
                if(cache > 0)                               // If there is something to paste
                {
                    p = 1 + count(current+cache, cache, n); // Paste Operation only (Recursive)
                }
                return c>p?p:c;                             // Returns the smallest number of operations
            }
        }
    
        int minSteps(int n) 
        {
            return count(1, 0, n);
        }
}; 
