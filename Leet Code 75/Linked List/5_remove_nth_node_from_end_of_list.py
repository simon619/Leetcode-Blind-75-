class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None


class LinkedList:

    def __init__(self):
        pass

    def build(self, head, data):
        if head.data is None:
            head.data = data
            return head
        else:
            header, last_node = head, head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(data)
            return header

    def printing(self, head):
        current_node = head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def elimination(self, head, length, pointer):
        ex_index = length - pointer
        prev, current_node, header = None, head, head
        counter = 0
        while current_node:
            if ex_index == 0:
                header = header.next
                break
            elif counter == ex_index:
                # print(current_node.data)
                prev.next = current_node.next
                break
            prev = current_node
            current_node = current_node.next
            counter += 1
        return header


if __name__ == '__main__':
    obj = LinkedList()
    list, pointer = [1, 2], 2
    root = Node(None)
    for i in list:
        root = obj.build(root, i)
    obj.printing(root)
    if len(list) <= 1 and pointer == 1:
        print([])
    else:
        root = obj.elimination(root, len(list), pointer)
        obj.printing(root)

