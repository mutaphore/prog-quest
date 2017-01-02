# Find missing element
----

## Problem
There is an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.


## Solution 1 - Python
Doesn't work if the sum of integers in array cause overflow
```python
A = [1,2,3,4,5,6,7,8,9,0]
B = [3,4,1,5,2,7,0,9,8]
# may overflow is sum is too big
print sum(A) - sum(B)
```

## Solution 2 - Python
Optimal O(N) solution
```python
A = [1,2,3,4,5,6,7,8,9,0]
B = [3,4,1,5,2,7,0,9,8]
result = 0
for num in A+B:
  result ^= num
print result
```