class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def unite(self, x, y):
        self.par[self.root(x)] = self.root(y)

    def root(self, x):
        self.par[x] = self.root(self.par[x]) if self.par[x] != x else x
        return self.par[x]
