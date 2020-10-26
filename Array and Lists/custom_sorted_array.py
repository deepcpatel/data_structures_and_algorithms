# Source: MathWorks Online Assesment [Snapshot in my Mobile Phone]

# Approach: Initialize Pointer from start and end of array. Move both of them closer and check 
# whether swap is needed or not. If swap is needed, increment the counter. Note that swap is needed
# when two left side number is odd and right side number is even in the array.

def initialization():
    return [5, 3, 6, 7, 1, 8, 9, 1, 6, 9, 15, 5, 9, 57, 2, 45, 23, 8]

def min_swaps(arr):
    start, end = 0, len(arr)-1
    counter = 0

    while start<end:
        if arr[start]%2 != 0 and arr[end]%2 == 0:
            arr[start], arr[end] = arr[end], arr[start]
            counter += 1
        else:
            if arr[start]%2 == 0:
                start += 1
            
            if arr[end]%2 != 0:
                end -= 1

    return arr, counter

if __name__ == '__main__':
    arr = initialization()
    sorted_arr, swaps = min_swaps(arr[:])
    print("Original Array:", arr)
    print("Sorted Array: ", sorted_arr)
    print("Minimum Swaps for Custom Sort:", swaps)