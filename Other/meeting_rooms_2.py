# Link: https://leetcode.com/problems/meeting-rooms-ii/
# Alternate Link: https://www.lintcode.com/problem/meeting-rooms-ii/

"""
Description:

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Example.

Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

"""

# Approach: We want to find overlaps. Divide intervals into two arrays -> start and end time. Sort both the arrays. Iteratively find number of start times smaller than
# end times and increment the counter or decrement the counter when end times smaller than start times. Keep a max_counter which records the highest value achieved by counter
# and return it.

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        start, end = [], []
        
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort() 
        end.sort()
        
        max_counter, counter = float('-inf'), 0
        i, j = 0, 0
        len_int = len(intervals)
       
        while i<len_int and  j<len_int:
            if start[i]<end[j]:
                counter += 1
                i += 1
            else:
                counter -= 1
                j += 1
            
            if max_counter<counter:
                max_counter = counter
                
        if j == len_int:
            while i<len_int:
                if start[i]<end[j]:
                    counter += 1
                    i += 1
            
                if max_counter<counter:
                    max_counter = counter
                
        return  max_counter