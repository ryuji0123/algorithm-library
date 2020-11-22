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
        # return t.get(self.eow, 0)

    def simSearch(self, word):
        stack = deque([(self.tree, 0, 0)])
        ret = 0
        while stack:
            t, idx, is_changed = stack.pop()
            if idx == len(word):
                ret += is_changed * t.get(self.eow, 0)
                continue

            if word[idx] in t:
                stack.append([t[word[idx]], idx + 1, is_changed])

            if is_changed == 1:
                continue

            for k in t.keys():
                if k != self.eow and k != word[idx]:
                    stack.append([t[k], idx + 1, 1])
        return ret

    def contain(self, word):
        t = self.tree
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return True


class Trie:

    def __init__(self):
        self.tree = {}
        self.sub = 'SUB'
        self.cached_tree = self.tree

    def add(self, word):
        t = self.tree
        for c in word:
            if c not in t:
                t[c] = {self.sub: []}

            t = t[c]
            t[self.sub].append(word)


    def incSearch(self, c):
        t = self.cached_tree
        if t is None or c not in t:
            self.cached_tree = None
            return []

        self.cached_tree = t[c]
        return self.cached_tree[self.sub]
