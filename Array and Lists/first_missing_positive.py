# Link: https://leetcode.com/problems/first-missing-positive/

'''
Approach: Consider following algorithm. It is linear time [O(2*n)]. It creates the array of same size as input and initially fill it with -1.
After. It scans original array and if nums[i] is positive and smaller than length(nums), it performs mark_array[nums[i]] = 1. This indicates that 
nums[i] number is present for us. After doing that, we again run a loop through mark_array and if a position is still -1, then that position value is missing from nums
as it is not marked as 1. Thus, we return the position value. This works on the logic of pigeonhole principle.

class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        mark_array = [-1]*l
        
        for n in nums:
            if n>0 and n<=l:
                mark_array[n-1] = 1
        
        for i in range(l):
            if mark_array[i] == -1:
                return i+1
        return l+1

However, the above algorithm is not inplace nad uses a O(n) memory. The following algorithm is inplace. It works on the same logic as above, bu instead of marking each
place as 1, we negate the value at that positon. And finally, we return the position having positive value remaining as it is not visited in previous loop. Had it been
present in nums, the position equal to that value would have been negated already.
'''
            
class Solution(object):
    def firstMissingPositive(self, nums):
        l = len(nums)
        
        for i in range(l):
            if nums[i] <= 0:
                nums[i] = 10e9
        
        for i in range(l):
            if abs(nums[i])>0 and abs(nums[i])<=l and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*=-1
        
        for i in range(l):
            if nums[i]>0:
                return i+1
        return l+1