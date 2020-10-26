# Link: https://leetcode.com/problems/evaluate-division/

# Approach: Document: ./archive/evaluate_division - Approach.pdf. Link: https://leetcode.com/problems/evaluate-division/discuss/629027/Python-Clean-Solution-from-DFS-O(mn)-to-Union-Find-O(m-%2B-n)-with-Explanation.
# Treat divison as graph and perform union-find for root of each divison.

class Solution(object):
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], old_parent = self.find(self.parent[x]), self.parent[x]
            self.value[x] = (self.value[x]*self.value[old_parent])/self.value[self.parent[x]]       # Updating New Value
        return self.parent[x]
    
    def union(self, numerator, denominator, value):
        if (numerator not in self.parent) and (denominator in self.parent):
            self.parent[numerator] = denominator
            self.value[numerator] = value
            self.size[numerator] = 1        # Children of parent
            self.size[denominator] += 1
        elif (denominator not in self.parent) and (numerator in self.parent):
            self.parent[denominator] = numerator
            self.value[denominator] = (1/value)
            self.size[denominator] = 1
            self.size[numerator] += 1
        elif (denominator not in self.parent) and (numerator not in self.parent):
            self.parent[numerator] = denominator
            self.parent[denominator] = denominator
            
            self.value[numerator] = value
            self.value[denominator] = 1
            
            self.size[numerator] = 1        # Children of parent
            self.size[denominator] = 2
        else:
            self.parent[numerator] = denominator
            self.value[numerator] = value
            self.size[denominator] += self.size[numerator]
        
        root_num = self.find(numerator)
        root_den = self.find(denominator)
        
        if root_num != root_den:
            if self.size[root_num]>self.size[root_den]:
                self.parent[denominaor] = root_num
                self.value[denominaor] = (self.value[denominaor]*self.value[root_den])/self.value[root_num]
                self.size[root_num] += 1
                self.size[root_den] -= 1
            else:
                self.parent[numerator] = root_den
                self.value[numerator] = (self.value[numerator]*self.value[root_num])/self.value[root_den]
                self.size[root_num] -= 1
                self.size[root_den] += 1
        
    def calcEquation(self, equations, values, queries):
        self.parent, self.value, self.size, ans = {}, {}, {}, []
        
        for e, v in zip(equations, values):
            self.union(e[0], e[1], v)
        
        for q in queries:
            if (q[0] not in self.parent) or (q[1] not in self.parent):
                ans.append(-1)
                continue
            
            root_q1 = self.find(q[0])
            root_q2 = self.find(q[1])
            
            if root_q1 != root_q2:
                ans.append(-1)
            else:
                ans.append(self.value[q[0]]/self.value[q[1]])
        
        return ans