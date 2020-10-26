# Link: https://leetcode.com/problems/third-maximum-number/

# Approach: Keep current 0th element in arr as 0th element in an 3 sized temp array (ar here). Keep rest float('-inf'). Now start iterating from second element in arr
# Follow the condition given below in line 14 and return the 3rd largest element from array or else largest element in an array if there are no 3 unique element in ar.

class Solution(object):
    def thirdMax(self, arr):
        ar = [arr[0], float('-inf'), float('-inf')]

        for i in range(1, len(arr)):
            if arr[i] == ar[0] or arr[i] == ar[1] or arr[i] == ar[2]:   # Skip when finding duplicates
                continue

            # Largest element finding condition
            if arr[i]>ar[0]:
                ar[2] = ar[1]
                ar[1] = ar[0]
                ar[0] = arr[i]
            elif arr[i]>ar[1]:
                ar[2] = ar[1]
                ar[1] = arr[i]
            elif arr[i]>ar[2]:
                ar[2] = arr[i]
            else:
                continue
                
        ret = (ar[2] if (ar[2] != float('-inf') and ar[1] != float('-inf')) else max(ar[0], ar[1], ar[2]))
        return ret