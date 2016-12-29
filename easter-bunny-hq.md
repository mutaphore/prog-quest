# Easter bunny HQ

## Problem
You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

## Solution 1
```python
moves = ["R8", "R4", "R4", "R8"]
compass = ["N", "E", "S", "W"]
curr_coord = (0, 0)
face = 0

for move in moves:
  direction = move[0]
  steps = int(move[1:])
  if direction == "R":
    face = (face + 1) % 4
  else:
    face = face - 1
    if face < 0:
      face = 3
  if compass[face] == "N":
    curr_coord = (curr_coord[0], curr_coord[1] + steps)
  elif compass[face] == "E":
    curr_coord = (curr_coord[0] + steps, curr_coord[1])
  elif compass[face] == "S":
    curr_coord = (curr_coord[0], curr_coord[1] - steps)
  else:
    curr_coord = (curr_coord[0] - steps, curr_coord[1])

print abs(curr_coord[0]) + abs(curr_coord[1])
```