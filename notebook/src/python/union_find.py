
class DisjointSet(object):

    def __init__(self, capacity):
        self.forest = list(range(capacity))

    def find(self, x):
        if self.forest[x] != x:
            self.forest[x] = self.find(self.forest[x])  # path compression
        return self.forest[x]

    def union(self, x, y):
        """
        :param x: disjoint set element
        :param y: disjoint set element
        :return: True on success (merged two sets),
                 False otherwise (already in one set)
        """
        setX, setY = self.find(x), self.find(y)
        if setX == setY:
            return False
        else:
            self.forest[setY] = setX
            return True


if __name__ == '__main__':
    ds = DisjointSet(10)
    print(ds.find(1))
    print(ds.find(2))
    ds.union(1, 2)
    print(ds.find(1))
    print(ds.find(2))
    ds.union(3, 4)
    print(ds.find(3))
    print(ds.find(4))
