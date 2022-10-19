class ConnectedComponents:

    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1] * size
        self.number_of_components = size

    def find_root(self, current_node):
        root = current_node
        while root != self.parents[root]:
            root = self.parents[root]

        while current_node != root:
            temp = self.parents[current_node]
            self.parents[current_node] = root
            current_node = temp
        return root

    def union_find(self, p, q):
        root_p, root_q = self.find_root(p), self.find_root(q)

        if root_p != root_q:
            if self.rank[root_p] < self.rank[root_q]:
                self.rank[root_q] += self.rank[root_p]
                self.rank[root_p] = 0
                self.parents[root_p] = root_p
            else:
                self.rank[root_p] += self.rank[root_q]
                self.rank[root_q] = 0
                self.parents[root_q] = root_p
            self.number_of_components -= 1


if __name__ == '__main__':
    list, num_of_nodes = [[0, 1], [1, 2], [3, 4]], 5
    obj = ConnectedComponents(num_of_nodes)
    for i, j in list:
        obj.union_find(i, j)
    print(obj.number_of_components)



