# Link: https://leetcode.com/problems/interleaving-string/

# Approach: Basically consider index_1, index_2 and index_3 the positional pointers of s1, s2 and s3 strings. Now, at every step choose whether alphabet at index_3 in s3 is s1[index_1] or s2[index_2].
# If it is index_1 and move on to next step and compare next alphabet in s3 i.e. s3[index_3+1] with s1[index_1+1] and s2[index_2]. If we had wrong choice (cannot move further since none of s1[new_index_1] 
# and s2[new_index_2] is matching to s3[new_index_3] now), then backtrack and choose index_2. Do this till all alphabets are exhausted. Now pair of (index_1, index_2) will sometimes repeat. in function 
# arguments. Thus store the results in dictionary against key "index_1_index_2" string as in line 27.

class Solution(object):
    
    def isInterleave(self, s1, s2, s3):
        ans_dict = {}
        
        def recur(idx1, idx2, idx3):
            key = str(idx1)+'_'+str(idx2)
            
            if idx1 == len(s1) and idx2 == len(s2) and idx3 == len(s3):
                return True
            elif key not in ans_dict:
                ans = False
                
                if idx1 < len(s1) and idx3 < len(s3) and s3[idx3] == s1[idx1]:
                    ans |= recur(idx1+1, idx2, idx3+1)
                
                if idx2 < len(s2) and idx3 < len(s3) and s3[idx3] == s2[idx2]:
                    ans |= recur(idx1, idx2+1, idx3+1)
                
                ans_dict[key] = ans
            return ans_dict[key]
        
        return recur(0, 0, 0)