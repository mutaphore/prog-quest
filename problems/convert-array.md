# Convert Array

## Problem
Given an array [a1, a2, …, aN, b1, b2, …, bN, c1, c2, …, cN]  convert it to [a1, b1, c1, a2, b2, c2, …, aN, bN, cN] in-place using constant extra space


## Python Solution 1
```python
def swap_index(cur_index, n):
  return (cur_index % 3)*n + (cur_index/3) 

def convert_array(arr):
  n = len(arr) / 3
  for cur in range(len(arr)):
    swap = swap_index(cur, n)
    while swap < cur:
      swap = swap_index(swap, n)
    arr[cur], arr[swap] = arr[swap], arr[cur]
  return arr
```
