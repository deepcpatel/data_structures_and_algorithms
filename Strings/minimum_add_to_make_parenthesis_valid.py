# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

# Approach: Add the "(" parenthesis to the stack. If ")" is ecountered in string and last element in stack is "(", then pop last element. Else add ")" well in the stack. At end of string iteration, coune the length
# of the stack and return it.

class Solution(object):
    def minAddToMakeValid(self, S):
        stack = []
        
        for i in range(len(S)):
            if S[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(S[i])
            else:
                stack.append(S[i])
        
        return len(stack)
