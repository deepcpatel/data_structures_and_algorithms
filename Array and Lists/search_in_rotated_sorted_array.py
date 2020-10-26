# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Approach: Binary search in the array. However, two cases would be possible. Rotated array (tested in line 15) and normal array (in line 26). In the normal case, run binary search as it is. In the first
# case, you have to set the range for element search (as sepicted in condition line 17, 18 and 23).

class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            
            if nums[mid]==target:
                return mid
            elif nums[end]<=nums[start]:
                if nums[mid]>=nums[end]:
                    if target<=nums[end] or target>=nums[mid]:
                        start = mid+1
                    else:
                        end = mid-1
                else:
                    if target>nums[end] or target<nums[mid]:
                        end = mid-1
                    else:
                        start = mid+1
            else:
                if nums[mid]>target:
                    end = mid-1
                else:
                    start = mid+1
        return -1

'''
# Compact solution by another person. Similar to mine but simplified.
# Solution link: (https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/617886/Python-Binary-Search-Solution-with-Explanation-~90)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[l]: return l
            elif target == nums[mid]: return mid
            elif target == nums[r]: return r
            
            if nums[mid] > nums[r]:
                if nums[l] < target < nums[mid]: r = mid - 1
                else: l = mid + 1
            else:
                if nums[mid] < target < nums[r]: l = mid + 1
                else: r = mid - 1
        return -1
'''
