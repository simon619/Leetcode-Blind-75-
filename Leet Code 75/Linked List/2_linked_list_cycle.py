class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        pass

    def adding(self, data, node):
        if node.data is None:
            node.data = data
            return node
        else:

            header, last_node = node, node
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)
            return header

    def print_func(self, root):
        current_node = root
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def cycle(self, node):
        current_node = node
        collector = set()
        while current_node:
            if current_node in set():
                return True
            collector.add(current_node)
            current_node = current_node.next
        return False

    def make_loop(self, root):
        current_node = root
        future = None
        while current_node:
            if current_node.data == 'e':
                future = current_node
            if current_node.data == 'b':
                temp = current_node.next
                current_node.next = root
                current_node.next.next = temp
            current_node = current_node.next


if __name__ == '__main__':
    obj = LinkedList()
    root = Node(None)
    l = ['a', 'b', 'c', 'd', 'e']
    for i in l:
        root = obj.adding(i, root)
    obj.print_func(root)
    obj.make_loop(root)
    obj.print_func(root)
    print(obj.cycle(root))
