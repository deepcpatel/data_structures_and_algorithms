# Link: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        
        if s == "" or s == " ":
            return True
        
        s = s.lower()
        
        while start<end:
            if s[start]== s[end]:
                end -= 1
                start += 1
            elif not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                 end -= 1
            else:
                return False
        return True