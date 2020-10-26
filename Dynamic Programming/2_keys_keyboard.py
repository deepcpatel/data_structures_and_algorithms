# Link: https://leetcode.com/problems/2-keys-keyboard/

# No Dynamic Programming

class Solution(object):
    def recur_num(self, num):
        result = 0
        for i in range(2, num+1):
            if num>1:
                count = 0
                while num%i==0:
                    num = num/i
                    count += 1
                result += count*i
            else:
                break
        return result
        
    def minSteps(self, n):
        return self.recur_num(n) 