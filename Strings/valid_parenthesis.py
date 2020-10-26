# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        li = []
        
        dic = {}
        dic['['] = ']'
        dic['{'] = '}'
        dic['('] = ')'
        dic[')'] = ''
        dic['}'] = ''
        dic[']'] = ''
        
        for i in range(len(s)):
            
            if(len(li) == 0):
                li.append(s[i])
            else:
                if dic[li[len(li)-1]] == s[i]:
                    li.pop()
                else:
                    li.append(s[i])
                    
        if(len(li)) == 0:
            return True
        else:
            return False 
