# Reference: https://stackoverflow.com/questions/54885971/more-efficient-method-of-finding-minimum-sum-after-k-operations

import math
import heapq 

def heapreplace_max(arr, item):
    ret, arr[0] = arr[0], item
    heapq._siftup_max(arr, 0)
    return ret

def min_sum(arr, K):
    temp_n, inp = 0, arr
    heapq._heapify_max(inp)    # Max Heapify

    for _ in range(K):
        temp_n = inp[0]
        heapreplace_max(inp, math.ceil(temp_n/2))
    return sum(inp)

if __name__ == '__main__':
    inp = [-9, 5, 6, -4, 7, -3, 8, 7, -1, 0, 10, 11, -12, 18]
    K = 6

    print(min_sum(inp, K))