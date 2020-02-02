class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.head.next = self.head

    def add_front(self, data):
        self.head.next = Node(data, next = self.head.next)
    
    def add_back(self, data):
        current_node = self.head.next
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = Node(data, next = current_node.next)

    def delete_front(self):
        temp = self.head.next
        self.head.next = temp.next
        temp.next = None

    def delete_back(self):
        current_node = self.head.next
        if current_node.next == self.head:
            self.head.next = self.head
            current_node.next = None
        else:
            while current_node.next.next != self.head:
                current_node = current_node.next
            temp = current_node.next
            current_node.next = self.head
            temp.next = None

    def insert_node(self, data, position):
        current_node = self.head.next
        current_position = 0
        while (
            current_position < position - 1 and
            current_node.next != self.head
        ):
            current_position = current_position + 1
            current_node = current_node.next
        current_node.next = Node(data, next = current_node.next)


    def delete_node(self, position):
        current_node = self.head.next
        current_position = 0
        while (
            current_position < position - 1 and
            current_node.next != self.head
        ):
            current_node = current_node.next
            current_position = current_position + 1
        temp = current_node.next
        current_node.next = temp.next
        temp.next = None