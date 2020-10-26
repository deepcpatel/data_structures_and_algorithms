# Link: https://leetcode.com/problems/top-k-frequent-words/

# Approach: Make dictionary to count all the words. After that push words along with their count to heap and heapify. After heapifying, extract the 
# First K elements from that.

import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        
        if words == [] or k == 0:
            return []
        
        word_table = {}
        heap, ans = [], []
        
        for w in words:
            word_table[w] = word_table.get(w,0) + 1
            
        for w in word_table.keys():
            heap.append((-word_table[w], w))
        
        heapq.heapify(heap)
        
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans