# Drawing Book

## Problem
Brie’s Drawing teacher asks her class to open their `n`-page book to page number `p`. Brie can either start turning pages from the front of the book (i.e., page number 1) or from the back of the book (i.e., page number n), and she always turns pages one-by-one (as opposed to skipping through multiple pages at once). When she opens the book, page 1 is always on the right side:

Each page in the book has two sides, front and back, except for the last page which may only have a front side depending on the total number of pages of the book (see the Explanation sections below for additional diagrams).

Given `m` and `n`, find and print the minimum number of pages Brie must turn in order to arrive at page .

### Sample input 1
```
6
2
```

### Sample output 1
```
1
```

### Sample input 2
```
5
4
```

### Sample output 2
```
0
```

## Solution
```python
import sys

n = int(raw_input().strip())
p = int(raw_input().strip())
# your code goes here

def check_front(p):
  left = 2
  flips = 1
  return (p - left) / 2 + 1

def check_back(n, p):
  if n % 2 == 0:
    right = n + 1
  else:
    right = n
  return (right - p) / 2

if n == 1:
  print 0
else:
  front = check_front(p)
  back = check_back(n, p)
  if front > back:
    print back
  else:
    print front
```