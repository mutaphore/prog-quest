#!/usr/bin/python

def reverse_words(s):
  words = s.strip().split()
  i = 0
  j = len(words) - 1
  while i <= j:
    words[i], words[j] = words[j], words[i]
    i += 1
    j -= 1
  return " ".join(words)

print reverse_words("I have  CS degree")