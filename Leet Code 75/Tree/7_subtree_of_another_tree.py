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

    def sub_tree(self, main_tree_node, sub_tree_node):
        if not sub_tree_node:
            return True
        if not main_tree_node:
            return False
        if self.is_subtree(main_tree_node, sub_tree_node):
            return True
        return (self.sub_tree(main_tree_node.left, sub_tree_node) or self.sub_tree(main_tree_node.right,
                                                                                  sub_tree_node))

    def is_subtree(self, main_tree_node, sub_tree_node):
        if not main_tree_node and not sub_tree_node:
            return True
        if main_tree_node and sub_tree_node and main_tree_node.data == sub_tree_node.data:
            return (self.is_subtree(main_tree_node.left, sub_tree_node.left) and self.is_subtree(main_tree_node.right,
                                                                                                sub_tree_node.right))
        return False


if __name__ == '__main__':
    main_list, sub_list = [3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]
    root1, root2 = None, None
    obj = TreeNode()
    root1, root2 = obj.build_tree(root1, main_list, 0), obj.build_tree(root2, sub_list, 0)
    print(obj.sub_tree(root1, root2))
