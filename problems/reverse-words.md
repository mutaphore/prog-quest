# Reverse Words in a String

## Problem
Given an input string, reverse all the words. To clarify, input: “Interviews are awesome!” output: “awesome! are Interviews”. Consider all consecutive non-whitespace characters as individual words. If there are multiple spaces between words reduce them to a single white space. Also remove all leading and trailing whitespaces. So, the output for ”   CS degree”, “CS    degree”, “CS degree   “, or ”   CS   degree   ” are all the same: “degree CS”.

### Sample Input 1
```python
s = "Interviews are awesome!"
```

## Python Solution 1
```python
def reverse_words(s):
  words = s.strip().split()
  i = 0
  j = len(words) - 1
  while i <= j:
    words[i], words[j] = words[j], words[i]
    i += 1
    j -= 1
  return " ".join(words)
```