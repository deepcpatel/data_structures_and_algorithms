# Link: https://leetcode.com/problems/maximum-subarray/

# Approach: Start summation of elements. At each step, identify whether it goes more than the max_sum, if so, update max_sum. At the same time, also, look that current sum is smaller than current element
# If so, we need to reset sum to 0 and start afresh from that index, because there is no point of considering previous elements which decrease sum value.

class Solution(object):
    def maxSubArray(self, nums):
        max_sum, asum, N = float('-inf'), 0, len(nums)
        
        if N == 0:
            return 0
        
        for i in range(N):
            asum += nums[i]
            
            if asum < nums[i]:
                asum = nums[i]
                
            if max_sum < asum:
                max_sum = asum
        
        return max_sum 