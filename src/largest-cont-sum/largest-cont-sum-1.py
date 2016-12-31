#!/usr/bin/python

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
