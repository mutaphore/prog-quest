# K-th Largest Element in Array

## Problem
Given an array of integers find the kth element in the sorted order (not the kth distinct element). So, if the array is [3, 1, 2, 1, 4] and k is 3 then the result is 2, because it’s the 3rd element in sorted order (but the 3rd distinct element is 3).

### Sample Input 1
```python
A = [3, 1, 2, 1, 4]
k = 3
# output 2
```

## Python Solution 1
Runtime in the worst case is O(N*log(N)) when k == N. On average it is O(k*log(N))
```python
from heapq import heapify, heappop

def kth_largest(arr, k):
  heapify(arr)
  cur = None
  for i in range(k):
    cur = heappop(arr)
  return cur
```

## Python Solution2
Since on average we partition array by half, this algorithm runs on average is O(N*log(N)), worst case is O(N^2)
```python
import random

def kth_largest(a, k): 
    left = 0 
    right = len(a) - 1 
    while left < right:
        rand = random.randint(left, right)
        new_pivot_ndx = partition_by_pivot(a, rand, left, right)
        if new_pivot_ndx == k-1:
            return a[new_pivot_ndx]
        elif new_pivot_ndx > k-1:
            right = new_pivot_ndx - 1
        else:
            left = new_pivot_ndx + 1
    return a[left]
   
def partition_by_pivot(a, pivot_ndx, left, right):
    a[right], a[pivot_ndx] = a[pivot_ndx], a[right]  
    pivot = a[right]
    new_pivot_ndx = -1
    for i in range(right):
        if a[i] > pivot:
            new_pivot_ndx += 1
            a[i], a[new_pivot_ndx] = a[new_pivot_ndx], a[i]
    new_pivot_ndx += 1
    a[right], a[new_pivot_ndx] = a[new_pivot_ndx], a[right]
    return new_pivot_ndx
```
