# Link: https://leetcode.com/problems/path-with-maximum-probability/

# Approach: This is simple Djikstra Shortest path algorithm, but, stop calculating shortest path when you reach to end node. However, little modifications is needed. Use heap to get the maximum 
# element till now. Previously, I used addary and searched the index having maximum probability, however, it was giving me time error. Moreover, intead of adding probability, multiply them to get
# probability of current path (line 37). Moreover, negate the probability when you entr into heap, because Python heap is min heap, and you want maximum element. Maintain a list which stores the
# maximum probability of path from start to the current node. Finally return the probability of start to end path (return 0 if it is negative infinity, it means that there is no path as it was 
# never visited).

import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        
        path_dic, cost, cost_ar = [[] for i in range(n)], [], [float('-inf')]*n
        
        for e, p in zip(edges, succProb):
            path_dic[e[0]].append((e[1], p))
            path_dic[e[1]].append((e[0], p))
        
        heapq.heappush(cost, (-1, start))
        cost_ar[start] = 1
        
        while cost:
            _, max_idx = heapq.heappop(cost)
            
            if max_idx == end:
                break
            
            for nei in path_dic[max_idx]:
                prob = cost_ar[max_idx]*nei[1]
                
                if prob>cost_ar[nei[0]]:
                    heapq.heappush(cost, (-prob, nei[0]))
                    cost_ar[nei[0]] = prob
            
        return (cost_ar[end] if cost_ar[end] > 0 else 0)