# Link: https://leetcode.com/problems/move-zeroes/

# Approach: First solution was finding zero index at first using while loop and then replacing non zero number with it. The second solution would update zero_index as it  iterates the array.
# Basically, it is not treating zero_idx as partition in the array. This means that the while loop in first solution could be of no use now.

class Solution(object):
    def moveZeroes(self, nums):
        num_len = len(nums)
        zero_idx = 0    # Partition
        
        '''
        # First solution
        for i in range(num_len):
            while zero_idx < num_len and nums[zero_idx] != 0:
                zero_idx += 1
                    
            if nums[i] != 0 and i>zero_idx and zero_idx < num_len:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
        '''
        
        # First solution
        for i in range(num_len):
            if nums[i] != 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
                
        return nums