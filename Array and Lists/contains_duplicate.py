# Link: https://leetcode.com/problems/contains-duplicate/

# Approach: Store numbers in hash tables (dictionaries) and if a number already exist in dictionary, then return True. Here, I directly converted
# my list into set (a form of hash table). Thus it will remove duplicates. Now, if size of set is smaller than input list, them some duplicates
# are removed, so we will return True else False.

class Solution(object):
    def containsDuplicate(self, nums):
        st = set(nums)
        
        if len(st)<len(nums):
            return True
        else:
            False