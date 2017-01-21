# Transform word

## Problem
Given a source word, target word and an English dictionary, transform the source word to target by changing/adding/removing 1 character at a time, while all intermediate words being valid English words. Return the transformation chain which has the smallest number of intermediate words.

### Sample Input 1
```python
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
```

## Python Solution 1
```python
def one_edit_distance(s1, s2):
  '''check if s1 is 1 edit distance away from s2'''
  if len(s1) < len(s2):
    s1, s2 = s2, s1
  if abs(len(s1) - len(s2)) > 1:
    return False
  if s1 == s2:
    return False
  edits = 0
  i = 0
  while i < len(s2):
    if s1[i] != s2[i]:
      edits += 1
      if len(s1) != len(s2):
        s2 = s2[:i] + s1[i] + s2[i:]
    if edits > 1:
      return False
    i += 1
  if len(s1) > len(s2) and edits == 1:
    return False
  return True

def build_graph(word_list):
  '''construct a graph of dictionary words where an edge exists between 2 nodes
  if there is a transoformation between them'''
  graph = {} # adjacency list
  for i in range(len(word_list)):
    for j in range(len(word_list)):
      if i == j:
        continue
      if one_edit_distance(word_list[i], word_list[j]):
        graph[word_list[i]] = graph.get(word_list[i], []) + [word_list[j]]
  return graph

def transform_word(start, end, word_list):
  word_list = list(set(word_list) | set([start, end]))
  g = build_graph(word_list)
  visited = {}  # visited nodes
  p = {}  # node parent for back tracing path
  d = {}  # distance from start
  d[start] = 0
  q = [start]  # queue
  # BFS to find shortest distance from start
  while len(q) > 0:
    u = q.pop(0)
    for v in g[u]:
      if not visited.get(v):
        d[v] = d[u] + 1
        p[v] = u
        q.append(v)
        if v == end:
          # backtrace path to start
          path = [end]
          cur = p[end]
          while cur != start:
            path = [cur] + path
            cur = p[cur]
          return [start] + path
    visited[u] = True
  return None

transform_word(begin_word, end_word, word_list)
```