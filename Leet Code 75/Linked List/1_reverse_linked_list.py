class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def adding(self, data):
        if not self.head:
            self.head = Node(data)
            return

        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def print_func(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse(self):
        def build(current, previous):
            if not current:
                return previous
            else:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                return build(current, previous)

        self.head = build(self.head, None)


if __name__ == '__main__':
    l = ['a', 'b', 'c', 'd', 'e']
    obj = LinkList()
    for i in l:
        obj.adding(i)
    obj.print_func()
    obj.reverse()
    obj.print_func()




