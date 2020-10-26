# Link: https://leetcode.com/problems/continuous-subarray-sum/

# Inspired Solution

# Approach: Take a remainder of current sum value (sum%k), let's say we got 5. Now perform sum of next digits and take remaindr each time. If you encounter same
# remainder 5 again at later position, then numbers between that range are summing to multiple of k. as (n*k + 5)%k == 5.

class Solution(object):
    
    def checkSubarraySum(self, nums, k):
        remainder = {}
        n, s = len(nums), 0
        
        if n<2:
            return False
        
        for i in range(n):
            s += nums[i]
            
            if k != 0:
                s = s%k
            
            if s == 0 and i>0:
                return True
            
            if s in remainder:
                if i-remainder[s]>1:
                    return True
            else:
                remainder[s] = i
        return False

'''
Inspirations (from discussion):

a). 
Basically you want to create an array of the accumulated sum, but instead of the sum, you have the sum%k. If you just go through it normally and return on sum%k == 0, then that only accounts for (n) possibilities out of (n^2) possibilities. However, if you find duplicated sum%k values, then that the sub array between those two indexes will actually be the solution.

i.e.
[4, 1, 2, 3] and 6

    1. if we get the accumulated sum, it looks like this [4, 5, 7, 10]
    2. if we make it accumulated sum % k, it looks like this [4, 5, 1, 4]
    3. notice that there is duplicated 4's. The diffference between these two sums in theory must be a multiple of 6 since we've only been storing the num%k.

Just wanted to write this out cz I thought it was pretty awesome and really couldn't figure it out for a while.

b).
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if (nums.size() < 2) return false;
        int sum = 0;
        unordered_map<int,int> sMap;
        
        // Idea is to check for a given remainder if same remainder already exists
        // if yes they should be atleast 1 index apart.
        // x*k + r be  1st sum and y*k + r be 2nd sum, do diffrence between them
        // is divisble by k , as (y*k + r) - (x*k + r) = (y-x)*k
        // both i and j should be atleast 1 index apart
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            
            // avoid % by 0 
            if (k != 0)
                sum = sum % k;
            
            // if sum remainde is 0, after first index it can be due to below condition
            // for e.g k = 6
            // a. 1,5  
            // b. 6,6
            // c. 0,6
            // In all above condition we are ensuring that atleast 2 numbers 
            // are contributing towards making number divisble
            if ((sum == 0) && i > 0) {
                return true;
            }
			
            // find if remainder has already been seen
            if (sMap.find(sum) != sMap.end()) {
                // if sum already found then check for diffrence in the indexes
                // remainders should be atleast 1 number apart then only valid.
                // for e.g k = 6 ,  1,2,12 is not valid, sum remainder are 1,3,3
                // below is valid 1,2,2,10, sum remainders are 1,3,5,3
                if ((i-sMap[sum]) > 1)
                    return true;
            } else 
                sMap[sum] = i;
        }
        return false;
    }        
};
'''