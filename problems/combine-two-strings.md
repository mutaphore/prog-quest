# Combine Two Strings

## Problem
We are given 3 strings: str1, str2, and str3. Str3 is said to be a shuffle of str1 and str2 if it can be formed by interleaving the characters of str1 and str2 in a way that maintains the left to right ordering of the characters from each string. For example, given str1=”abc” and str2=”def”, str3=”dabecf” is a valid shuffle since it preserves the character ordering of the two strings. So, given these 3 strings write a function that detects whether str3 is a valid shuffle of str1 and str2.

### Sample Input 1
```python
str1 = "abc"
str2 = "def"
str3 = "dabecf"
# True
```

### Sample Input 2
```python
str1 = "abbc"
str2 = "debb"
str3 = "adebbbbc"
# True
```

### Sample Input 3
```python
str1 = "aabbc"
str2 = "dafg"
str3 = "aaadbbcfg"
# False
```

## Python Solution 1
```python
def is_valid_shuffle(s1, s2, s3, cur):
  x = s3[cur]
  l = None
  r = None
  if len(s1) > 0:
    l = s1[0]
  if len(s2) > 0:
    r = s2[0]
  # base case
  if cur == len(s3)-1 and (l == x or r == x):
    return True
  if l != r:
    # go down the branch where we have a match with s3
    if l == x:
      return is_valid_shuffle(s1[1:], s2, s3, cur+1)
    elif r == x:
      return is_valid_shuffle(s1, s2[1:], s3, cur+1)
    else:
      return False
  else:
    # s1 and s2 are equal, try all possible branches
    if l == x:
      return (is_valid_shuffle(s1[1:], s2, s3, cur+1) or
        is_valid_shuffle(s1, s2[1:], s3, cur+1))
    else:
      return False

is_valid_shuffle(str1, str2, str3, 0)
```