# Link: https://leetcode.com/problems/interval-list-intersections/

# Approach: Allocate two pointers to list A and B iteratively. Run a while loop until one of the pointer reaches the end. At each iteration, select the intervals pointed to by the pointers. Check if
# Overlap between intervals exist. If it exist then calculate the overlap interval and append ot to the final_list. If not, the go to next step. In the next step, drop the interval having smaller end 
# time and select the next one in that list and repeat the same procedure. Finally, return the final_list.

class Solution(object):
    def intervalIntersection(self, A, B):
        pointer_1, pointer_2, la, lb, final_li = 0, 0, len(A), len(B), []
        
        while pointer_1 < la and pointer_2 < lb:
            int_1, int_2 = A[pointer_1], B[pointer_2]   # Select the intervals
            
            if not (int_2[0]>int_1[1] or int_1[0]>int_2[1]):  # If overlap between two intervals exist
                overlap = max(int_1[0], int_2[0]), min(int_1[1], int_2[1])  # Find the overlap interval
                final_li.append(overlap)
            
            if int_2[1]<int_1[1]:   # Drop the interval which has smaller end time and select the next one
                pointer_2 += 1
            else:
                pointer_1 += 1
            
        return final_li