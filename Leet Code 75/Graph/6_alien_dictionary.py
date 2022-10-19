class Node:
    def __init__(self, data):
        self.data = data
        self.adj = ""


class AlienDictionary:

    def __init__(self):
        self.visited = {}
        self.ordered = ""

    def constrains_checking(self, list):
        neig = {j: set() for i in list for j in i}
        for i in range(len(list) - 1):
            word1, word2 = list[i], list[i + 1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    neig[word1[j]].add(word2[j])
                    break
        print(neig)
        return self.graph_building(neig)

    def graph_building(self, graph):
        list, dic = [], {}
        for node in graph:
            new_node = Node(node)
            list.append(new_node)
            dic[node] = new_node
        for key, val in graph.items():
            dic[key].adj = [dic[ad] for ad in val]
        return self.topological_sort(list)

    def dfs(self, current_node):
        if current_node in self.visited:
            return self.visited[current_node]
        self.visited[current_node] = True
        for nei in current_node.adj:
            if self.dfs(nei):
                return True
        self.visited[current_node] = False
        self.ordered += str(current_node.data)

    def topological_sort(self, node_list):
        for node in node_list:
            if self.dfs(node):
                return ""
        return self.ordered[::-1]


if __name__ == '__main__':
    list = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    obj = AlienDictionary()
    print(obj.constrains_checking(list))

