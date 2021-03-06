# Median of Integer Stream 

## Problem
Given a stream of unsorted integers, find the median element in sorted order at any given time. So, we will be receiving a continuous stream of numbers in some random order and we don’t know the stream length in advance. Write a function that finds the median of the already received numbers efficiently at any time. We will be asked to find the median multiple times. Just to recall, median is the middle element in an odd length sorted array, and in the even case it’s the average of the middle elements.

## Python Solution 1
O(log(N)) because using heaps
```python
import heapq

max_heap = []
min_heap = []

def calc_median(num, count):
  med = None
  if len(min_heap) > 0 and num > min_heap[0]:
    heapq.heappush(min_heap, num)
    # rebalance if needed
    if len(min_heap) - len(max_heap) > 1:
      heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
  else:
    # multiply by -1 to get max heap
    heapq.heappush(max_heap, -1 * num)
    # rebalance if needed
    if len(max_heap) - len(min_heap) > 1:
      heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
  if count % 2 == 0:
    med = (-1 * max_heap[0] + float(min_heap[0])) / 2
  else:
    med = -1 * max_heap[0]
  return med

with open('input.txt', 'r') as f:
  count = 0
  for line in f:
    count += 1
    print calc_median(int(line), count)
```
