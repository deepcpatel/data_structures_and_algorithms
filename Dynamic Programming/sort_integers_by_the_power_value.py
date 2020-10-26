# Link: https://leetcode.com/problems/sort-integers-by-the-power-value/

# Approach: Dynamic Programming approach (Memoization). Recursively iterate to all the intermediate numbers. In mid-way, store power to reach 1 for each intermediate number. Next time,
# if same intermediate number is encountered, just retrieve its power value from stored dictionary. Used heap sort to retrieve Kth element, but found minimal runtime change in my code.

import heapq

class Solution(object):
    def even_pow(self, x):
        return x//2
    
    def odd_pow(self, x):
        return (3*x)+1
    
    def next_num(self, x):
        if x%2 == 0:
            return self.even_pow(x)
        else:
            return self.odd_pow(x)
        
    def recur_opr(self, x):
        if x not in self.pow_dict:              # Checking whether number is already existing or not
            nxtn = self.next_num(x)
            nxtpow = self.recur_opr(nxtn)
            self.pow_dict[x] = nxtpow + 1       # Memoizing
        return self.pow_dict[x]
        
    def getKth(self, lo, hi, k):
        ans_list, el = [], None
        self.pow_dict = {1:0, 2:1}
        
        for i in range(lo, hi+1):
            power = self.recur_opr(i)
            ans_list.append((power, i))
        
        heapq.heapify(ans_list)
        
        for i in range(k):
            el = heapq.heappop(ans_list)
            
        return el[1]

'''
# Faster Code - Same Approach
# Link: https://leetcode.com/problems/sort-integers-by-the-power-value/discuss/629544/Faster-than-90-of-Python-online-submissions

class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        dp = {1:0,2:1}

        def getPower(n):
            if n in dp:
                return dp[n]
            r = 1 + (getPower(n / 2) if n % 2 == 0 else getPower(n * 3 + 1))
            dp[n] = r
            return dp[n]
        
        res = [_ for _ in range(lo, hi + 1)]
        res = sorted(res, key = getPower)
        return res[k - 1]
'''