// Link: https://leetcode.com/problems/subarray-product-less-than-k/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm> 
#include <sstream>

using namespace std;

class Solution
{
    public:
        int numSubarrayProductLessThanK(vector<int>& nums, int k)
        {
            int N = nums.size(), start = 0, end = 0, mult = 1, prev_end = -1, counter = 0;
            
            while(start <= end and end < N)
            {
                // cout<<start<<", "<<end<<", "<<mult*nums[end]<<"\n";
                if(prev_end != end)
                {
                    if(nums[end] < k)
                    {
                        counter++;
                    }
                    else
                    {
                        prev_end = end;
                        end++;
                        start = end;
                        mult = 1;
                        continue;
                    }
                }
                
                if(mult*nums[end] < k)
                {
                    counter += (end-start);
                    mult *= nums[end];
                    prev_end = end;
                    end++;

                }
                else
                {
                    mult /= nums[start];
                    prev_end = end;
                    start++;
                }
            }
            return counter;
        }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        getline(cin, line);
        int k = stringToInteger(line);
        
        int ret = Solution().numSubarrayProductLessThanK(nums, k);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}