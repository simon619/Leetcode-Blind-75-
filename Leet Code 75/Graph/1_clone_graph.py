class Node:

    def __init__(self, data):
        self.data = data
        self.neighbore = []


class Graph:
    def __init__(self):
        pass

    def clone(self, node):
        old_node_to_new = {}

        def dfs(node):
            if node in old_node_to_new:
                return old_node_to_new[node]
            copy_node = Node(node.data)
            old_node_to_new[node] = copy_node
            for neigh in node.neighbor:
                copy_node.neighbore.append(dfs(neigh))
            return copy_node

        return dfs(node) if node else None


if __name__ == '__main__':
    obj = Graph()
    list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node_dic, node_list = {}, []
    for i in range(1, len(list) + 1):
        node = Node(i)
        node_dic[i] = node
        node_list.append(node)

    for i in range(len(list)):
        for j in range(len(list[i])):
            node_list[i].neighbore.append(node_dic[list[i][j]])
    copied_node = obj.clone(node_list[0])
    print(copied_node.data)
    print(copied_node.neighbore[1].data)
