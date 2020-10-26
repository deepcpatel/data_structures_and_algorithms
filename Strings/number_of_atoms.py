# Link: https://leetcode.com/problems/number-of-atoms/

class Solution(object):
    def __init__(self):
        self.atoms = {}
        self.form = ""
        self.form_size = -1
        
    def count_atoms(self, idx):
        i = idx
        li = []
        lin = []
        st_char = ''
        st_num = ''
        while i<self.form_size and self.form[i]!=')':
            if self.form[i].isupper():
                if st_char != '':
                    add = 0
                    if st_num == '':
                        add = 1
                    else:
                        add = int(st_num)
                        
                    li.append(st_char)
                    lin.append(add)
                    st_char = ''
                    st_num = ''
                st_char += self.form[i]
            elif self.form[i].islower():
                st_char += self.form[i]
            elif self.form[i].isdigit():
                st_num += self.form[i]
            else:   # '('
                l1, l2, i = self.count_atoms(i+1)
                li.extend(l1)
                lin.extend(l2)
            i += 1
        
        if st_char != '':
            add = 0
            if st_num == '':
                add = 1
            else:
                add = int(st_num)

            li.append(st_char)
            lin.append(add)
        
        if i<(self.form_size-1):
            if self.form[i] == ')' and self.form[i+1].isdigit():
                s = ''
                for j in range(i+1, self.form_size):
                    if not self.form[j].isdigit():
                        break
                    s+=self.form[j]
                    i += 1
                n = int(s)
                for k in range(len(lin)):
                    lin[k] *= n
        return li, lin, i
                
    def countOfAtoms(self, formula):
        ans = ''
        self.form = formula
        self.form_size = len(formula)
        li, lin, _ = self.count_atoms(0)
        
        for name, num in zip(li, lin):
            if name not in self.atoms:
                self.atoms[name] = num
            else:
                self.atoms[name] = self.atoms[name] + num
        
        k_s = list(self.atoms.keys())
        k_s.sort()
        
        for k in k_s:
            ans += k
            if self.atoms[k] > 1:
                ans += str(self.atoms[k])
        return ans