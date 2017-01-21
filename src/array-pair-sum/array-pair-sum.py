#!/usr/bin/python

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
