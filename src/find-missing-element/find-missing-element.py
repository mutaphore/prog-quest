#!/usr/bin/python

A = [1,2,3,4,5,6,7,8,9,0]
B = [3,4,1,5,2,7,0,9,8]

# may overflow is sum is too big
print sum(A) - sum(B)

# optimal solution
result = 0
for num in A+B:
  result ^= num
print result