# Link: https://leetcode.com/problems/counting-bits/

# Approach: Basically, after every power(2) position (eg: 2, 4, 8, 16 ...), I add 1 to all the previous offset positions (equal to current power of two). For eg consider initial array [0, 1]. Now since its
# length is 2 (pwer of two), my third position will be (1 + ans[3-offset]) which is 1 + 0 (as offset is currently two). My fourth position value will be (1 + ans[4-offset]), which is 1 + 1, as offset is 2).
# Now since length of ans == 4, offst will set to 4. Now my fifth value will be (1 + ans[5-offset]) which will be (1 + 0, as offset is 4) and so on.

class Solution(object):
    def countBits(self, num):
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        
        ans, offset = [0]*(num+1), 2
        ans[1] = 1
        
        for i in range(2, num+1):
            ans[i] = 1+ans[i-offset]
            
            if (i+1) == offset*2:
                offset = offset*2
        
        return ans