class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        self.traversed = []
        self.queue = []

    def find_index(self, inorder, num):
        for i in range(len(inorder)):
            if inorder[i] == num:
                return i

    def build_tree(self, node, preorder_list, inorder_list):
        if not preorder_list or not inorder_list:
            return None
        node = Node(preorder_list[0])
        mid_index = self.find_index(inorder_list, preorder_list[0])
        node.left = self.build_tree(node.left, preorder_list[1: mid_index + 1], inorder_list[:mid_index])
        node.right = self.build_tree(node.left, preorder_list[mid_index + 1:], inorder_list[mid_index + 1:])
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
    obj = TreeNode()
    root = None
    preorder, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    root = obj.build_tree(root, preorder, inorder)
    obj.level_order_traversal(root)
    print(obj.traversed)
