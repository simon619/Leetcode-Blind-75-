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

    def inorder_traversal(self, node, traversal_list):
        if node:
            traversal_list = self.inorder_traversal(node.left, traversal_list)
            traversal_list += str(node.data)
            traversal_list = self.inorder_traversal(node.right, traversal_list)
        return traversal_list


if __name__ == '__main__':
    list, k = [5, 3, 6, 2, 4, None, None, 1], 3
    root = None
    obj = TreeNode()
    root = obj.build_tree(root, list, 0)
    if k not in list:
        print("k is missing")
    else:
        trav_st = obj.inorder_traversal(root, '')
        kth_index = trav_st.index(str(k))
        print(kth_index + 1)
