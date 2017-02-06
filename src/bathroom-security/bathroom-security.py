
key_pad = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

key_pad2 = [
[0, 0, 1, 0, 0],
[0, 2, 3, 4, 0],
[5, 6, 7, 8, 9],
[0, 'A', 'B', 'C', 0],
[0, 0, 'D', 0, 0]
]

def move_right(i, j):
  if j < 4 and key_pad2[i][j+1] != 0:
    j += 1
  return i, j

def move_left(i, j):
  if j > 0 and key_pad2[i][j-1] != 0:
    j -= 1
  return i, j

def move_up(i, j):
  if i > 0 and key_pad2[i-1][j] != 0:
    i -= 1
  return i, j

def move_down(i, j):
  if i < 4 and key_pad2[i+1][j] != 0:
    i += 1
  return i, j

code = []
i = 2
j = 0
with open('input.txt', 'r') as f:
  for line in f:
    for c in line:
      if c == 'U':
        i, j = move_up(i, j)
      elif c == 'D':
        i, j = move_down(i, j)
      elif c == 'L':
        i, j = move_left(i, j)
      elif c == 'R':
        i, j = move_right(i, j)
    code.append(key_pad2[i][j])

print code
