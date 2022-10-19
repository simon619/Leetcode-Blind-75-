class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head1 = None
        self.head2 = None
        self.head = None

    def head1_building(self, data):
        if self.head1 is None:
            self.head1 = Node(data)
            return
        else:
            last_node = self.head1
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def head2_building(self, data):
        if self.head2 is None:
            self.head2 = Node(data)
            return
        else:
            last_node = self.head2
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)

    def printing(self, node):
        current_node = node
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def marging(self, link1, link2):
        current_node = None
        while link1 and link2:
            if link1.data < link2.data:
                if not self.head:
                    self.head = link1
                    current_node = self.head
                else:
                    current_node.next = link1
                    current_node = current_node.next
                link1 = link1.next
            else:
                if not self.head:
                    self.head = link2
                    current_node = self.head
                else:
                    current_node.next = link2
                    current_node = current_node.next
                link2 = link2.next

        while link1:
            if not current_node and not self.head:
                self.head = link1
                current_node = self.head
            else:
                current_node.next = link1
                current_node = current_node.next
            link1 = link1.next

        while link2:
            if not current_node and not self.head:
                self.head = link2
                current_node = link2
            else:
                current_node.next = link2
                current_node = current_node.next
            link2 = link2.next


if __name__ == '__main__':
    obj = LinkedList()
    l1, l2 = [], [0]
    for i in l1:
        obj.head1_building(i)
    for j in l2:
        obj.head2_building(j)
    obj.printing(obj.head1)
    obj.printing(obj.head2)
    obj.marging(obj.head1, obj.head2)
    obj.printing(obj.head)
