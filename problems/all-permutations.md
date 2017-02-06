# All permutations of string

## Problem
Generate all permutations of a given string.

## Python Solution 1
```python
def helper(s, index, cur, perms):
    if index == len(s):
        return perms.append(cur)
    for i in range(len(cur)+1):
        tmp = cur[0:i] + s[index] + cur[i:]
        helper(s, index+1, tmp, perms)

def all_perms(s):
    if len(s) < 2:
        return s
    perms = []
    helper(s, 1, s[0], perms)
    return perms

perms = all_perms("abcd")
print perms
```