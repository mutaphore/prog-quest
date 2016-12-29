# Matrix Region Sum

## Problem
Given a matrix of integers and coordinates of a rectangular region within the matrix, find the sum of numbers falling inside the rectangle. Our program will be called multiple times with different rectangular regions from the same matrix.

## Solution 1 - Python
Always take O(M*N) time
```python
# inputs
mat = [[1,2,3],[4,5,6],[7,8,9]]
coords = [[0,0], [0,2], [1,0], [1,2]]

def region_sum(mat, coords):
  a, b, c, d = coords
  total = 0
  for i in range(a[0], d[0]+1):
    for j in range(a[1], d[1]+1):
      total += mat[i][j]
  return total
```

## Solution 2 - Python
O(M*N) initially, O(1) for every call after that
```python
# inputs
mat = [[1,2,3],[4,5,6],[7,8,9]]
coords = [[0,0], [0,2], [1,0], [1,2]]

def precompute_sums(mat):
  # use dynamic programming technic to precompute matrix sums
  cache_mat = [[0 for i in range(w)] for j in range(h)]
  w = len(mat[0])
  h = len(mat)
  for i in range(w):
    for j in range(h):
      if i == 0 and j == 0:
        cache_mat[j][i] = mat[j][i]
      elif i == 0 and j != 0:
        cache_mat[j][i] = mat[j][i] + cache_mat[j-1]
      elif i != 0 and j == 0:
        cache_mat[j][i] = mat[j][i] + cache_mat[i-1]
      else:
        cache_mat[j][i] = mat[j][i] + cache_mat[j][i-1] + cache_mat[j-1][i] - cache_mat[j-1][i-1]

def region_sum(mat, coords):
  a, b, c, d = coords
  if a[0] == 0 or a[1] == 0:
    oa = 0
  else:
    oa = cache_mat[a[1]][a[0]]
  if a[0] == 0:
    oc = 0
  else:
    oc = cache_mat[c[1]][c[0]]
  if a[1] == 0:
    ob = 0
  else:
    ob = cache_mat[b[1]][b[0]]
  return cache_mat[d[1]][d[0]] - ob - bc + oa

cache_mat = precompute_sums(mat)
print region_sum(mat, coords)
```