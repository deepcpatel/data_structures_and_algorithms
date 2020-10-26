# Link: https://leetcode.com/problems/two-sum/

# Approach: Add all the numbers in the dictionary with corresponding index in the array. Now again start iterating over elements in the array. Perform num = target-array[i].
# If the num is in dictionary then extract its position (let's say j) and return (i, j).

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        
        for i in range(len(nums)):
            dic[nums[i]] = i
            
        for i in range(len(nums)):
            if target-nums[i] in dic:
                j = dic[target-nums[i]]
                if i != j:
                    return [min(i, j), max(i, j)]