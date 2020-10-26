# Link: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        start = 0
        end = 0
        
        num_sum = 0
        max_sum = float('-inf')
        
        while start<=end and end<len(nums):
            
            num_sum += nums[end]
            
            if nums[end]>num_sum:
                start = end
                num_sum = nums[start]
            
            if num_sum>max_sum:
                max_sum = num_sum
            end+=1
        return max_sum 
