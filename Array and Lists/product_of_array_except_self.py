# Link: https://leetcode.com/problems/product-of-array-except-self/

# Approach: Calculate A Forward Array and a Backward array of multiplication. Example: if input = [1, 2, 3, 4], forward_array = [1, 2, 6, 24] and backward_array = [24, 24, 12, 4].
# Now, ans[i] = forward_array[i-1]*backward_array[i+1]. To make constant space, instead of making forward_array and backward_array, perform forward and backward operation on nums itself and 
# a single new array named 'output' respectively. Finally, modify output as shown in line 22 to calculate final answer.

class Solution(object):
    def productExceptSelf(self, nums):
        len_ar = len(nums)
        output = [1]*len_ar
        
        output[-1] = nums[-1]
        
        for i in range(1, len_ar):
            output[len_ar-1-i] = output[len_ar-i]*nums[len_ar-1-i]
        
        for i in range(1, len_ar):
            nums[i] = nums[i-1]*nums[i]
        
        output[0] = output[1]
        for i in range(1, len_ar-1):
            output[i] = output[i+1]*nums[i-1]
        output[-1] = nums[-2]
        return output 