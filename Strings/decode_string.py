# Link: https://leetcode.com/problems/decode-string/

# Approach: Use Resursion to handle each [] and return the output after processing it.

class Solution(object):
    def recur_str(self, number, string, idx):
        i = idx
        res = ''
        num = ''
        while i < len(string) and string[i] != ']':
            if string[i].isdigit():
                num += string[i]
            elif string[i] == '[':
                out, i = self.recur_str(int(num), string, i+1)
                res += out
                num = ''
            else:
                res += string[i]            
            i += 1
        return number*res, i
    
    def decodeString(self, s):
        ans, _ = self.recur_str(1, s, 0)
        return ans