# Link: https://leetcode.com/problems/sliding-window-maximum/

# Approach: Make a queue to store indices of the array. Now, iterate over the array elements. At every position check whether element at position stored last in queue is smaller than current element
# nums[queue[-1]]<nums[i]. If it is, then pop that position from queue till this condition is true. Basically this makes space in queue for storing maximum elements in the current window in increasing 
# order. After this condition is not invalid, exit the while loop and att the current index i in the queue. If i is the first element in the queue, then it is maximum element in the window so far and 
# if i is second, then it is second maximum element in the window so far and similar for all subsequent elements in the queue. Now, if first element in the queue is more than k distance far away from
# current i, then pop it as it is no longer in the window of size k. Now, if current i is greater than k (minimum window size), then add the element at position which is stored first in the queue 
# (maximum element so far) in the answer list. Finally return the answer list.

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue, li = deque(), []
        
        for i in range(len(nums)):            
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            
            queue.append(i)
            
            if i-queue[0] >= k:
                queue.popleft()
        
            if i >= (k-1):
                li.append(nums[queue[0]])
            
        return li