class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

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

    def max_depth(self, node):
        if node is None:
            return 0
        else:
            left = self.max_depth(node.left)
            right = self.max_depth(node.right)
            return 1 + max(left, right)

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


if __name__ == '__main__':
    list = [3, 9, 20, None, None, 15, 7]
    obj = TreeNode()
    root = None
    root = obj.build_tree(root, list, 0)
    print(obj.__noorder_traversal__(root))
    print(obj.max_depth(root))
