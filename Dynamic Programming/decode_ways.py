# Link: https://leetcode.com/problems/decode-ways/

from functools import lru_cache

class Solution(object):
        
    def numDecodings(self, s: str) -> int:
        n = len(s)
        li = [-1]*(n+1)
        li[n] = 1
        
        @lru_cache(None)
        def ways(i: int) -> int:
            if li[i] == -1:
                count = 0
                
                if i+1<n+1:
                    if int(s[i:i+1])>0:
                        count += ways(i+1)
                    else:
                        li[i] = count
                        return li[i]
                    
                if i+2<n+1:
                    if int(s[i:i+2])<27:
                        count += ways(i+2)
                li[i] = count
            return li[i]
        
        return ways(0) 