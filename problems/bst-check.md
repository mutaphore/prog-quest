# Binary Search Tree Check

## Problem
Given a binary tree, check whether it’s a binary search tree or not.

## Python Solution 1
O(N) pre-order traversal
```python
class Node():
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def is_bst_helper(root, mi, mx):
  if root == None:
    return True
  if root.val < mx and root.val >= mi:
    left = is_bst_helper(root.left, mi, root.val)
    right = is_bst_helper(root.right, root.val, mx)
    return left and right
  else:
    return False

def is_bst(root):
  if root == None:
    return True
  return (is_bst_helper(root.left, -float("inf"), root.val) and 
    is_bst_helper(root.right, root.val, float("inf")))
```
