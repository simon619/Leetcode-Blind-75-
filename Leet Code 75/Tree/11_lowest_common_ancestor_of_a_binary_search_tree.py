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

    def find_lcs(self, node, p, q):
        if node:
            if node.data > p and node.data > q:
                if node.left:
                    return self.find_lcs(node.left, p, q)
                else:
                    return node.data
            elif node.data < p and node.data < q:
                if node.right:
                    return self.find_lcs(node.right, p, q)
                else:
                    return node.data
            else:
                return node.data


if __name__ == '__main__':
    obj = TreeNode()
    list, p, q = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4
    root = None
    root = obj.build_tree(root, list, 0)
    print(obj.find_lcs(root, p, q))
