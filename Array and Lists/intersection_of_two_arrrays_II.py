# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Approach: Basically, find all common elements from two arrays (not necessary subsequences). Two approaches are there. (1). Sort both arrays and find common elements, (2). Store elements of longer array
# in hash table along with occurences. Now, start iterating small array and decrease each occurence from hash table of corresponding number. Add number to ans_list if occurences is non zero.

class Solution(object):
    def intersect(self, nums1, nums2):
        # Using Sort (Fast when both the arrays are sorted)
        ans_list = []
        
        nums1.sort()    # No need to do this if both the arrays are already sorted
        nums2.sort()
        
        idx1, idx2 = 0, 0
        
        if len(nums1)<len(nums2):
            while idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] == nums2[idx2]:
                    ans_list.append(nums1[idx1])
                    idx1 += 1
                    idx2 += 1
                else:
                    while idx2<len(nums2) and nums1[idx1] != nums2[idx2]:
                        if nums1[idx1]<nums2[idx2]:
                            idx1 += 1
                            break
                        idx2 += 1
        else:
            while idx1 < len(nums1) and idx2 < len(nums2):
                if nums1[idx1] == nums2[idx2]:
                    ans_list.append(nums1[idx1])
                    idx1 += 1
                    idx2 += 1
                else:
                    while idx1<len(nums1) and nums1[idx1] != nums2[idx2]:
                        if nums2[idx2]<nums1[idx1]:
                            idx2 += 1
                            break
                        idx1 += 1
        
        return ans_list
    
'''
# Using Hashing (Fast when both arrays are unsorted)
def intersect(self, nums1, nums2):
    dict1 = {}
    result =[]
    if len(nums2)>len(nums1):
        nums1,nums2 = nums2, nums1
    for i in nums1:
        dict1[i]=dict1.get(i,0)+1
    for i in nums2:
        if i in dict1 and dict1[i]>0:
            result.append(i)
            dict1[i] -=1
    return result
'''