# Link: https://leetcode.com/problems/plus-one/

# Approach: Start adding from last element. Increase size in beginning if carry is left


class Solution(object):
    def plusOne(self, digits):
        len_dig = len(digits)        
        carry = 1
        
        for i in range(len_dig-1, -1, -1):
            digits[i] += carry
            carry = digits[i]/10
            
            if carry>0:
                digits[i] %= 10
            else:
                break
        
        if carry>0:
            t_l = [carry]
            t_l.extend(digits)
            return t_l
        else:
            return digits

'''
# Fast method
k =0
k = int(''.join(str(e) for e in digits)) +1
return list(map(int, str(k)))
''' 