#!/usr/bin/python

# A = [-1, 3, 2, -4, 8, 0, -9, 7, -5, 6]
A = [1, 2, 3, 4, -6, 7, 7, 7]

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