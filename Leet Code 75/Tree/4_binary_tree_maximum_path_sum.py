class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        self.path_sum = 0

    def build_tree(self, node, list, current_pointer):
        left_pointer, right_pointer = 2 * current_pointer + 1, 2 * current_pointer + 2
        if node is None:
            node = Node(list[current_pointer])
        if left_pointer < len(list):
            node.left = self.build_tree(node.left, list, left_pointer)
        if right_pointer < len(list):
            node.right = self.build_tree(node.right, list, right_pointer)
        return node

    def __noorder_traversal__(self, node):
        current_node = node
        q = [current_node]

        def __traversal__(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                if info.left:
                    q.append(info.left)
                if info.right:
                    q.append(info.right)
                traversal = __traversal__(q, traversal)
            return traversal

        result = __traversal__(q, '')
        return result

    def max_path_sum_dfs(self, node):
        if not node or not node.data:
            return 0
        left_val = self.max_path_sum_dfs(node.left)
        right_val = self.max_path_sum_dfs(node.right)
        left_val, right_val = max(left_val, 0), max(right_val, 0)
        self.path_sum = max(self.path_sum, node.data + left_val + right_val)

        return node.data + max(left_val, right_val)


if __name__ == '__main__':
    obj = TreeNode()
    root, list = None, [-10, 9, 20, None, None, 15, 7]
    root = obj.build_tree(root, list, 0)
    print(obj.__noorder_traversal__(root))
    obj.path_sum = root.data
    for_nothing = obj.max_path_sum_dfs(root)
    print(obj.path_sum)
