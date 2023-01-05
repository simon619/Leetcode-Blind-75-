class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        pass

    def build_tree(self, node, list, current_pointer):
        if len(list) == 0:
            return None
        if not list[current_pointer]:
            return None
        left_pointer, right_pointer = 2 * current_pointer + 1, 2 * current_pointer + 2
        if node is None:
            node = Node(list[current_pointer])
        if left_pointer < len(list):
            node.left = self.build_tree(node.left, list, left_pointer)
        if right_pointer < len(list):
            node.right = self.build_tree(node.right, list, right_pointer)
        return node

    def level_traversal(self, node):
        current_node = node
        q = [current_node]

        def traversal_func(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                if info.left:
                    q.append(info.left)
                if info.right:
                    q.append(info.right)
                traversal = traversal_func(q, traversal)
            return traversal

        result = traversal_func(q, '')
        return result

    def validation(self, node):
        if not node:
            return True
        if node.left and node.right:
            if not (node.data > node.left.data) or not (node.data < node.right.data):
                return False
        return self.validation(node.left) and self.validation(node.right)


if __name__ == '__main__':
    obj = TreeNode()
    root = None
    list = [2, 1, 3]
    root = obj.build_tree(root, list, 0)
    print(obj.level_traversal(root))
    print(obj.validation(root))
