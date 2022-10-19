class Node:
    def __init__(self, data):
        self.data = data
        self.neighbor = []


class ValidTree:
    def __init__(self):
        self.visited = set()

    def buildthegraph(self, list):
        if not len(list):
            return True
        node_set = set()
        for i, j in list:
            if i not in node_set:
                node_set.add(i)
            if j not in node_set:
                node_set.add(j)
        node_dic = {i: Node(i) for i in range(len(node_set))}
        for i, j in list:
            node_dic[i].neighbor.append(node_dic[j])
            node_dic[j].neighbor.append(node_dic[i])
        return self.validation(len(node_set), node_dic[0])

    def dfs(self, current_node, previous_node):
        if current_node in self.visited:
            return False
        self.visited.add(current_node)
        for neig in current_node.neighbor:
            if neig == previous_node:
                continue
            if not self.dfs(neig, current_node):
                return False
        return True

    def validation(self, n, root):
        return self.dfs(root, None) and n == len(self.visited)


if __name__ == '__main__':
    obj = ValidTree()
    list = [[0, 1], [0, 2], [0, 3], [1, 4]]
    root_node = obj.buildthegraph(list)
    print(root_node)
