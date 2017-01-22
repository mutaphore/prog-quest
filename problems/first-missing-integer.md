# First missing integer

## Problem
Let A be an array of length n. Design an algorithm to find the smallest positive integer which is not present in A. You do not need to preserve the contents of A.

### Sample Input 1
```python
A = [3, 5, 4, -1, 5, 1, -1]
# returns 2
```

## Python Solution 1
```python
def first_missing(arr):
  n = len(arr)
  for i in range(n):
    k = arr[i]
    if k > 0 and k < n and arr[k-1] != k:
      arr[k-1], arr[i] = arr[i], arr[k-1]
  for i in range(n):
    if arr[i] != i+1:
      return i+1
  return n+1
```
