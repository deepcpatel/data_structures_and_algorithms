# Link: https://leetcode.com/problems/house-robber/

# Approach: Used Tabulation method (Dynamic Programming). In this, max robbery at each house i can be done by robbing house i + MAX of i-2 or i-3 house.

class Solution(object):
    def rob(self, nums):
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) > 2:
            nums[2] = nums[2] + nums[0]
        
        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])