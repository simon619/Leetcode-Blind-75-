class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        pass

    def build(self, head, data):
        if head.data is None:
            head.data = data
            return head
        else:
            header, current_node = head, head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)
            return header

    def print(self, head):
        current_node = head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def get_to_middle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_plus = slow.next
        previous = slow.next = None

        def reverse(current, prev):
            if not current:
                return prev
            else:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                return reverse(current, prev)

        second = reverse(mid_plus, previous)
        return second

    def reorder(self, first, second):
        header = first
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        return header


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    obj = LinkedList()
    head = Node(None)
    for i in list:
        head = obj.build(head, i)
    second = obj.get_to_middle(head)
    reorder_head = obj.reorder(head, second)
    obj.print(reorder_head)
