class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    head = None
    tail = None

    def append_node_right(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            if self.tail == self.head:
                self.tail = Node(data = data, prev = self.head)
                self.head.next = self.tail
            else:
                new_node = Node(data = data)
                temp = self.tail
                temp.next = new_node
                new_node.prev = temp
                self.tail = new_node

    def append_node_left(self, data):
        new_node = Node(data = data, next = self.head)
        self.head = new_node

    def delete_node_right(self):
        if self.tail == None:
            raise Exception('cant remove tail of None')
        temp = self.tail
        self.tail = temp.prev
        temp.prev = None
        self.tail.next = None
  
    def delete_node_left(self):
        if self.head == None:
            raise Exception('cant remove head of None')
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None

    def insert_node(self, data, position):
        current_node = self.head
        current_position = position
        while current_position < position:
            if current_node == None:
                raise Exception('position too high')
            else:
                current_node = current_node.next
                current_position = current_position + 1
        new_node = Node(data = data, prev = current_node.prev, next = current_node)
        current_node.prev.next = new_node
        current_node.prev = new_node

    def delete_node(self, position):
        current_node = self.head
        current_position = 0
        while current_position < position:
            if current_node == None:
                raise Exception('position too high')
            else:
                current_node = current_node.next
                current_position = current_position + 1
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node.prev = None
        current_node.next = None