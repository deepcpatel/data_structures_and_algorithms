# Link: https://leetcode.com/problems/find-median-from-data-stream/

# Approach: Make two heap - max_heap and min_heap. max_heap stores Maximum among smaller numbers and min_heap stores minimum among bigger numbers.
# Smaller and bigger number is decided based on the previous median. Also, if new number is greater than median, add it to min_heap and if it is 
# smaller, then add it to max_heap [Line 32]. Now, also check that difference of size of both the heaps do not exceed 2 (i.e. len(min_heap)-len(max_heap) < 2
# and len(max_heap)-len(min_heap) < 2) [Line 41]. If it exceeds then transfer first element from larger heap to the smaller heap and update the median [Line 49].

import heapq

class MedianFinder(object):
    def __init__(self):
        self.max_heap = []  # Stores Maximum among smaller numbers (bigger and smaller is decided by current median)
        self.min_heap = []  # Stores Minimum among bigger numbers
        self.median = 0
        
    def _heappush_max(self, heap, item):
        """Maxheap version of a heappush."""
        heap.append(item)
        heapq._siftdown_max(heap, 0, len(heap)-1)
        
    def _heappop_max(self, heap):
        """Maxheap version of a heappop."""
        lastelt = heap.pop()
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            heapq._siftup_max(heap, 0)
            return returnitem
        return lastelt
        
    def addNum(self, num):
        # Adding new element
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
            self.median = num
        elif num < self.median:
                self._heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balancing both the heaps
        if (len(self.min_heap)-len(self.max_heap))>1:
            temp = heapq.heappop(self.min_heap)
            self._heappush_max(self.max_heap, temp)
        elif (len(self.max_heap)-len(self.min_heap))>1:
            temp = self._heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, temp)
            
        # Calculating new median
        if len(self.min_heap) == len(self.max_heap):
            self.median = (self.min_heap[0] + self.max_heap[0])/2.0
        elif len(self.min_heap) > len(self.max_heap):
            self.median = self.min_heap[0]
        else:
            self.median = self.max_heap[0]
            
    def findMedian(self):
        return self.median
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 