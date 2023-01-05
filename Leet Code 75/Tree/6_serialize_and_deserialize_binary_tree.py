class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        self.traversed = []
        self.queue = []

    def serialize(self, node):
        current_node = node
        q = [current_node]

        def __traversal__(q, traversal):
            if q:
                info = q.pop(0)
                traversal += str(info.data) + '->'
                # q.append(info.left) if info.left else traversal += "None" + '->'
                # q.append(info.right) if info.right else traversal += "None" + '->'
                if info.left:
                    q.append(info.left)
                else:
                    traversal += "None" + '->'
                if info.right:
                    q.append(info.right)
                else:
                    traversal += "None" + '->'
                traversal = __traversal__(q, traversal)
            return traversal

        result = __traversal__(q, '')
        return result

    def deserialize(self, node, list, current_pointer):
        if len(list) == 0:
            return None
        if not list[current_pointer]:
            return None
        left_pointer, right_pointer = 2 * current_pointer + 1, 2 * current_pointer + 2
        if node is None:
            node = Node(list[current_pointer])
        if left_pointer < len(list):
            node.left = self.deserialize(node.left, list, left_pointer)
        if right_pointer < len(list):
            node.right = self.deserialize(node.right, list, right_pointer)
        return node


if __name__ == '__main__':
    obj = TreeNode()
    list = [1, 2, 3, None, None, 4, 5]
    root = None
    root = obj.deserialize(root, list, 0)
    print(obj.serialize(root))
