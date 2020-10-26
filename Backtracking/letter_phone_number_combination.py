# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Approach: Recursive Backtracking

class Solution(object):
    def init_digit_dic(self):
        self.dl = {}
        self.dl['2'] = ['a', 'b', 'c']
        self.dl['3'] = ['d', 'e', 'f']
        self.dl['4'] = ['g', 'h', 'i']
        self.dl['5'] = ['j', 'k', 'l']
        self.dl['6'] = ['m', 'n', 'o']
        self.dl['7'] = ['p', 'q', 'r', 's']
        self.dl['8'] = ['t', 'u', 'v']
        self.dl['9'] = ['w', 'x', 'y', 'z']
        
    def letter_combination(self, idx, digits, string):
        if idx >= len(digits):
            self.ans_list.append(string)
        else:
            for i in self.dl[digits[idx]]:
                self.letter_combination(idx+1, digits, string+i)
    
    def letterCombinations(self, digits):
        if digits == "":
            return []
        
        self.init_digit_dic()
        self.ans_list = []
        self.letter_combination(0, digits, '')
        return self.ans_list 
