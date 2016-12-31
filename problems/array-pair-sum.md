# Array pair sum
----

## Problem
Given an integer array, output all pairs that sum up to a specific value k.

## Python Solution 1
O(N^2)
```python
A = [1, 3, 5, 7, 9, 11]
k = 10
pairs = []
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[i]+A[j] == k:
          pairs.append((A[i], A[j]))
print pairs
```

## Python Solution 2
O(N)
```python
A = [1, 3, 5, 7, 9, 11]
k = 10
h = {}
result = {}

for i in A:
    h[k-i] = i 
for i in A:
    if i in h:
        t = None
        if h[i] <= i:
            t = (h[i], i)
        else:
            t = (i, h[i])
        result[t] = 1 

print result.keys()
```