# Link: https://leetcode.com/problems/partition-array-for-maximum-sum/

# Approach: # Bottom Up Approach (Tabular Method) in Dynamic Programming. Basically, we want to partition array A into at max K sized chunks. For each chunk, all the cell in it will then be overwritten
# by maximum number in that chunk. After that, calculate sum of all elements in the array A. Our strategy should be to partition array such that it yields maximum sum. Let's say we build an dp array 
# (here max_sum) of size len(A), which at ith position stores maximum sum achieved till ith position in A. This is done by line 19 and 20 in following code. From ith position, it goes back K places
# using 'for j in range(i-1, i-K-1, -1)' loop and compares current max_sum and the sum if array was partitioned at jth position. This way we fill up max_sum array and return its last element. 

class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        max_sum, arr_len, max_num = [-1]*len(A), len(A), -1
        
        for i in range(K):
            max_num = max(A[i], max_num)
            max_sum[i] = max_num*(i+1)
        
        for i in range(K, arr_len):
            max_num, max_sum[i] = A[i], A[i]
            
            for j in range(i-1, i-K-1, -1):
                    max_sum[i] = max(max_sum[j] + max_num*(i-j), max_sum[i])
                    max_num = max(max_num, A[j])
                    
        return max_sum[-1]