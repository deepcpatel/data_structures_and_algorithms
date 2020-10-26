# Link: https://leetcode.com/problems/single-number/

# Approach: Start from 0th position and subsequently perform XOR. Same numbers would cancel out and single number will remain.

class Solution(object):
    def singleNumber(self, nums):
        n = nums[0]
        l = len(nums)
        
        for i in range(1, l):
            n = n^nums[i]
        return n