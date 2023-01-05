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

    def same_tree(self, first_tree_node, second_tree_node):
        if not first_tree_node and not second_tree_node:
            return True
        if (not first_tree_node or not second_tree_node) or (first_tree_node.data != second_tree_node.data):
            return False
        return (self.same_tree(first_tree_node.left, second_tree_node.left) and self.same_tree(first_tree_node.right,
                                                                                               second_tree_node.right))


if __name__ == '__main__':
    obj = TreeNode()
    list1, list2 = [1, 2, 1], [1, 1, 2]
    root1, root2 = None, None
    root1, root2 = obj.build_tree(root1, list1, 0), obj.build_tree(root2, list2, 0)
    print(obj.same_tree(root1, root2))
