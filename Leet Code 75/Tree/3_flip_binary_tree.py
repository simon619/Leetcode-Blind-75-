class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class InverseTree:

    def __init__(self):
        pass

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

    def inverse(self, root):
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.inverse(root.left)
        self.inverse(root.right)
        return root


if __name__ == '__main__':
    obj = InverseTree()
    list = [4, 2, 7, 1, 3, 6, 9]
    root = None
    root = obj.build_tree(root, list, 0)
    print(f'Tree: {obj.__noorder_traversal__(root)}')
    new_root = obj.inverse(root)
    print(f'Inversed Tree: {obj.__noorder_traversal__(new_root)}')

