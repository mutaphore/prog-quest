# Largest continuous sum

## Problem
Given an array of integers (positive and negative) find the largest continuous sum.

## Solution 1 - Python
O(N^2)
```python
A = [-1, 3, 2, -4, 8, 0, -9, 7, -5, 6]

largest = -float("inf")
start = 0
end = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        s = sum(A[i:j+1])
        if s > largest:
            largest = s
            start = i
            end = j

print sum(A[start:end+1])
print (start, end)
```

## Solution 2 - Python
O(N)
```python
A = [-1, 3, 2, -4, 8, 0, -9, 7, -5, 6]

curSum = maxSum = A[0]
start = 0
end = 0
for i in range(1, len(A)):
    if curSum + A[i] >= A[i]:
        curSum = curSum + A[i]
    else:
        curSum = A[i]
        start = end = i
    if maxSum < curSum:
        maxSum = curSum
        end = i

print maxSum
print (start, end)
```