# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Approach: Keep two pointers one iterating array and one that only increments when new elements found (current_element > previous_array)

class Solution(object):
    def removeDuplicates(self, nums):
        real_prog = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[real_prog] = nums[i]
                real_prog += 1
        return real_prog 