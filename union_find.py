class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def unite(self, x, y):
        self.par[self.root(x)] = self.root(y)

    def root(self, x):
        self.par[x] = self.root(self.par[x]) if self.par[x] != x else x
        return self.par[x]

class UnionFind:
    def __init__(self):
        self.par = {}

    def unite(self, x, y):
        self.par[x] = self.par.setdefault(x, x)
        self.par[y] = self.par.setdefault(y, y)
        self.par[self.root(x)] = self.root(y)

    def root(self, x):
        self.par[x] = self.root(self.par[x]) if self.par[x] != x else x
        return self.par[x]
