# Compute parity

## Problem
How to compute parity of a very large number?

## Solution 1 - Python
O(N) where N is number of bits
```python
def compute_parity(num):
  result = 0
  while num:
    result ^= (num & 1)
    num >>= 1
  return result
```

## Solution 2 - Python
O(k) where k is the number of set bits in number
```python
def compute_parity(num):
  result = 0
  while num:
    # remove lowest bit in num
    num &= (num - 1)
    result ^= 1
  return result
```