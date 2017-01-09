# Dictionary anagrams

## Problem
Given a dictionary of English words, find all sets of anagrams. For instance "pots", "stop" and "tops" are all anagrams of one another because each can be formed by permuting the letters of the others.

## Solution 1 - python
```python
words = ["pots", "stop", "tops", "bat", "tat", "tab", "cab"]
maps = {}
for word in words:
  sig = "".join(sorted(word))
  maps[sig] = maps.get(sig, []) + [word]
print maps.values()
```
