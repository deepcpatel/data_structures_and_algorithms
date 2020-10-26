# Link: https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1/

# Approach: Start from beginning of the array. Make a dictionary to store the address of x and y. Now at every index i, if arr[i] == x or y, save it to addict[x] or addict[y] respectively. At same time
# maintain a min_dist variable to store the minimum distance. Update as in condition min_dist = min(min_dist, abs(addict[x]-addict[y])). Return min_dist at end or -1 if any of x or y is -1 in addict.

def minDist(arr, n, x, y):
    addict, min_dist = {x:-1, y:-1}, float('inf')
    
    for i in range(n):
        if arr[i] == x:
            addict[x] = i
            
            if addict[y] != -1:
                min_dist = min(min_dist, abs(addict[x]-addict[y]))
                
        if arr[i] == y:
            addict[y] = i
            
            if addict[x] != -1:
                min_dist = min(min_dist, abs(addict[x]-addict[y]))
                
    if addict[x] == -1 or addict[y] == -1:
        return -1
    else:
        return min_dist