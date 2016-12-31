#!/usr/bin/python

from trie import Trie

words = ["cat", "cats", "catsdogcats", "catxdogcatsrat", "dog", 
         "dogcatsdog", "hippopotamuses", "rat", "ratcat", 
         "ratcatdog", "ratcatdogcat", "ratcatdogcatcatz"]

# insert words into Trie
t = Trie()
for word in words:
    t.insert(word)

# find longest compound word
q = []
for word in words:
    prefixes = t.getPrefixesForWord(word)
    for prefix in prefixes:
        item = { "original": word, "postfix": word[len(prefix):] } 
        q.append(item)
longest_compound_word = ""
while len(q) > 0:
    item = q.pop(0) 
    word = item["postfix"]
    prefixes = t.getPrefixesForWord(word)
    for prefix in prefixes:
        postfix = word[len(prefix):]
        if postfix == "" and len(item["original"]) > len(longest_compound_word):
            longest_compound_word = item["original"]
        else:
            item["postfix"] = postfix
            q.append(item)
print longest_compound_word
