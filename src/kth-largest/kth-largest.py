#!/usr/bin/python

import random

def kth_largest(a, k):
    left = 0
    right = len(a) - 1
    while left < right:
        rand = random.randint(left, right)
        new_pivot_ndx = partition_by_pivot(a, rand, left, right)
        if new_pivot_ndx == k-1:
            return a[new_pivot_ndx]
        elif new_pivot_ndx > k-1:
            right = new_pivot_ndx - 1
        else:
            left = new_pivot_ndx + 1
    return a[left]

def partition_by_pivot(a, pivot_ndx, left, right):
    a[right], a[pivot_ndx] = a[pivot_ndx], a[right]  
    pivot = a[right]
    new_pivot_ndx = -1
    for i in range(right):
        if a[i] > pivot:
            new_pivot_ndx += 1
            a[i], a[new_pivot_ndx] = a[new_pivot_ndx], a[i]
    new_pivot_ndx += 1
    a[right], a[new_pivot_ndx] = a[new_pivot_ndx], a[right]
    return new_pivot_ndx


a = [6,3,7,2,8,1,5,4,4]

for i in range(1, 10):
    print kth_largest(a, i)
