from node import Node

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.isTerminal = True

    def getPrefixesForWord(self, word):
        prefixes = [] 
        prefix = ""
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                break
            cur = cur.children[c]
            prefix = prefix + cur.letter
            if cur.isTerminal:
                prefixes.append(prefix)
        return prefixes

