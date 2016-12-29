#!/usr/bin/python

# moves = ["R2", "L5", "L4", "L5", "R4", "R1", "L4"]
# moves = ["R5", "L5", "R5", "R3"]
# moves = ["R2", "L3"]
# moves = ["R2", "R2", "R2"]
# moves = ["R8", "R4", "R4", "R8"]

f = open("input.txt", "r")
moves = map(lambda s: s.strip(), f.readline().split(","))

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