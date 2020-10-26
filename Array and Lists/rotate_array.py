# Link: https://leetcode.com/problems/rotate-array/
# Link: https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/

# Approach: Reverse array from 0 to l and again reverse from 0 to k and k to l. If k is greater than l the we only need k-l shifts to simulate k rotations (line 15).

class Solution(object):
    def reverse_array(self, s, e, array):
        while s<e:
            array[s], array[e] = array[e], array[s]
            s += 1
            e -= 1
    
    def rotate(self, nums, k):
        l = len(nums)
        
        if k >= l:
            k = k - l
            
        self.reverse_array(0, l-1, nums)
        self.reverse_array(0, k-1, nums)
        self.reverse_array(k, l-1, nums)
        return nums