# Link: https://leetcode.com/problems/3sum/

# My Solution
# Approach: Divide given list into two sets. Each set contains positive number and negative numbers (also set ensures no duplication). Make a dictionary to count frequency
# of our numbers in input list. After that, for each positive number in positive set and each negative number in negative set, calculate 'ans' and look that whether it 
# is in our num_dict (frequency dictionary). If it exist, then form triplet and append it to final_answer. Make final_answer to be set to ensure no duplication in answer

class Solution(object):
    def threeSum(self, nums):
        neg_set = set()
        pos_set = set()
        final_ans = set()
        num_dict = {}
        
        for i in range(len(nums)):
            num_dict[nums[i]] = num_dict.get(nums[i], 0) + 1
            if nums[i]<0:
                neg_set.add(nums[i])
            else:
                pos_set.add(nums[i])
                
        if num_dict.get(0, 0)>2:
            final_ans.add((0, 0, 0))
                
        for pos in pos_set:
            for neg in neg_set:
                ans = -(pos + neg)
                tup = (pos, neg)
                
                if (ans in tup and num_dict[ans]>1) or (ans not in tup and ans in num_dict):
                    final_ans.add(tuple(sorted([pos, neg, ans])))
        return final_ans
