# Link: https://leetcode.com/problems/combination-sum/

# Approach: It is backtracking based solution. The care that is to be taken care is to avoid duplicate combinations (not permutations). For example, [2, 3, 2] is same as [2, 2, 3].
# Thus, we only need [2, 2, 3] as our answer. To do that, when you reach an index, don't start doing recursion from precedding index. Start directly from current (as duplicates are
# allowed) or next index.

class Solution(object):
    def recur(self, target, candidates, temp_list, ans_list, start):
        if target > 0:
            for i in range(start, len(candidates)):
                if target-candidates[i] >= 0:
                    temp_list.append(candidates[i])
                    self.recur(target-candidates[i], candidates, temp_list, ans_list, i)
                    temp_list.pop()
        else:
            ans_list.append(list(temp_list))
        
    def combinationSum(self, candidates, target):
        ans_list = []
        self.recur(target, candidates, [], ans_list, 0)
        return ans_list