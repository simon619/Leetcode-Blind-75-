class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        self.traversed = []
        self.queue = []

    def build_tree(self, node, list, current_pointer):
        if len(list) == 0:
            return None
        left_pointer, right_pointer = 2 * current_pointer + 1, 2 * current_pointer + 2
        if node is None:
            node = Node(list[current_pointer])
        if left_pointer < len(list):
            node.left = self.build_tree(node.left, list, left_pointer)
        if right_pointer < len(list):
            node.right = self.build_tree(node.right, list, right_pointer)
        return node

    def level_order_traversal(self, root):
        if root:
            self.queue.append(root)
            while self.queue:
                current_level = []
                for n in range(len(self.queue)):
                    cur_node = self.queue.pop(0)
                    if cur_node and cur_node.data:
                        current_level.append(cur_node.data)
                        self.queue.append(cur_node.left)
                        self.queue.append(cur_node.right)
                if current_level:
                    self.traversed.append(current_level)


if __name__ == '__main__':
    list = [1]
    root = None
    obj = TreeNode()
    root = obj.build_tree(root, list, 0)
    obj.level_order_traversal(root)
    print(obj.traversed)
