// Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution 
{
    private:
        map<int, vector<char>> book;
        vector<string> ans;
        vector<int> no;
        int no_length = 0;
    
    public:
        void init_dict()
        {
            book.insert(make_pair(2, vector<char>({'a', 'b', 'c'})));
            book.insert(make_pair(3, vector<char>({'d', 'e', 'f'})));
            book.insert(make_pair(4, vector<char>({'g', 'h', 'i'})));
            book.insert(make_pair(5, vector<char>({'j', 'k', 'l'})));
            book.insert(make_pair(6, vector<char>({'m', 'n', 'o'})));
            book.insert(make_pair(7, vector<char>({'p', 'q', 'r', 's'})));
            book.insert(make_pair(8, vector<char>({'t', 'u', 'v'})));
            book.insert(make_pair(9, vector<char>({'w', 'x', 'y', 'z'})));
        }
    
        vector<string> letterCombinations(string digits)
        {
            no_length = digits.length();
            
            if(no_length == 0)
            {
                return ans;
            }
            
            init_dict();
            
            for(int i=0;i<no_length;i++)
            {
                no.push_back(digits[i]-48);
            }
            
            explore(0, "");
            return ans;
        }
    
        void explore(int idx, string prev)
        {   
            if(idx >= no_length)
            {
                ans.push_back(prev);
                return;
            }
            
            for(int i=0; i<book[no[idx]].size();i++)
            {
                explore(idx+1, prev+book[no[idx]][i]);
            }
        }
}; 
