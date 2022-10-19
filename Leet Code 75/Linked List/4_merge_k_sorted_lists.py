class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        pass

    def receive(self, list):
        def building(head, data):
            if head.data is None:
                head.data = data
                return head
            else:
                header, last_node = head, head
                while last_node.next:
                    last_node = last_node.next
                last_node.next = Node(data)
                return header

        head = Node(None)
        for i in list:
            head = building(head, i)
        return head

    def printing(self, head):
        current_node = head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def merging(self, list1, list2):
        head = None
        current_node = None
        while list1 and list2:
            if list1.data < list2.data:
                if head is None:
                    head = list1
                    current_node = head
                else:
                    current_node.next = list1
                    current_node = current_node.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    current_node = head
                else:
                    current_node.next = list2
                    current_node = current_node.next
                list2 = list2.next

        while list1:
            if not current_node and not head:
                head = list1
                current_node = head
            else:
                current_node.next = list1
                current_node = current_node.next
            list1 = list1.next

        while list2:
            if not current_node and not head:
                head = list2
                current_node = head
            else:
                current_node.next = list2
                current_node = current_node.next
            list2 = list2.next
        return head


if __name__ == '__main__':
    obj = LinkedList()
    list = [[1, 4, 5], [1, 3, 4], [2, 6]]
    ll = []
    for i in list:
        ll.append(obj.receive(i))
    merged_list = [ll[0]]
    if len(ll) <= 1:
        print(obj.printing(ll[0]))
    else:
        for i in range(1, len(ll)):
            merged_list[0] = obj.merging(merged_list[0], ll[i])
        obj.printing(merged_list[0])
