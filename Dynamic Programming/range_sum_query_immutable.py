# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Approach: Preprocess array by cumulative addition of each cell (adding sum of previous cells at current cell). To process query, use formula given in line 15.

class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        
        for i in range(1, self.N):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, i, j):
        return self.nums[j] - (self.nums[i-1] if i else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)