class Node:
    def __init__(self, letter=None, isTerminal=False):
        self.letter = letter
        self.isTerminal = isTerminal
        self.children = {}

    def __str__(self):
        s = self.letter
        if self.isTerminal:
            s += "*"
        return s
