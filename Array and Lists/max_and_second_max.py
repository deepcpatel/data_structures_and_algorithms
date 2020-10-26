# Link: https://practice.geeksforgeeks.org/problems/max-and-second-max/1/

# Approch: Maintain an array to store max and second max elements. Now initialize the max in array with arr[0] and rest with -1. Now iterate arr from 1 to len(arr).
# When you encounter an element in arr[i] that is equal to any element in li, skip it. Else, if arr[i] is greater than li[0], replace li[0] with arr[i] after replacing 
# li[1] with li[0] because li[0] now become second largest element. Similarly, if an arr[i]>li[1], straight away replace li[1] with arr[i]. Finally return li[1].

# Function to find largest and second largest element in the array
def largestAndSecondLargest(sizeOfArray, arr):
    li = [arr[0], -1]

    for i in range(1, sizeOfArray):
        if arr[i] == li[0] or arr[i] == li[1]:
            continue
        
        if arr[i]>li[0]:
            li[1] = li[0]
            li[0] = arr[i]
        elif arr[i]>li[1]:
            li[1] = arr[i]
    
    return li