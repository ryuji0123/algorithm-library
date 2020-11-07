class Trie:
    def __init__(self):
        self.tree = {}
        self.eow = 'EOW'

    def add(self, word):
        t = self.tree
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t[self.eow] = t.get(self.eow, 0) + 1

    def search(self, word):
        t = self.tree
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return True if self.eow in t else False

    def contain(self, word):
        t = self.tree
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return True
