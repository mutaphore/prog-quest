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
