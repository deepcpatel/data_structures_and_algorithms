# Link: https://leetcode.com/problems/k-concatenation-maximum-sum/

# Will concate the given array with itself first. Then, will calculate max sum subarray from it.
# We then see that, will this (max_sum + remaining numbers in array) if added k/2 times is actually greater than the max_sum.
# If it is, then we return the former, otherwise later one.

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        li = []
        li.extend(arr)
        
        if k > 1:
            li.extend(arr)
        
        s = 0
        max_sum = 0
        summ = 0

        for i in range(len(li)):
            s += li[i]
            summ += li[i]
            
            if li[i]>s:
                s = li[i]
            
            if s>max_sum:
                max_sum = s
                
        rem = summ - max_sum
        val = (int((k/2.0)*(rem+max_sum))-rem)
        
        if  val > max_sum:
            return val % (10**9+7)
        else:
            return max_sum % (10**9+7)