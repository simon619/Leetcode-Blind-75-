class UniquePath:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def traversing(self, way1, way2):
        if way1 == self.row or way2 == self.col:
            return 0
        elif way1 == self.row - 1 and way2 == self.col - 1:
            return 1
        else:
            return self.traversing(way1 + 1, way2) + self.traversing(way1, way2 + 1)


if __name__ == '__main__':
    obj = UniquePath(3, 7)
    print(obj.traversing(0, 0))
