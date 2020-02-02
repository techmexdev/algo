class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    head = None

    def append_node_right(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def append_node_left(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def delete_node_right(self):
        if self.head == None:
            raise Exception('cant delete nodes')
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            temp = current_node.next
            current_node.next = None
            return temp

    def delete_node_left(self):
        if self.head == None:
            raise Exception('cant delete nodes')
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp

    def insert_node(self, position, data):
        if position == 0:
            self.append_node_left(data)
        else:
            current_node = self.head
            current_position = 0
            while current_position < position - 1:
                if current_node.next == None:
                    raise Exception('position too high')
                else:
                    current_node = current_node.next
                    current_position = current_position + 1
            new_node = Node(data, current_node.next)
            current_node.next = new_node


    def delete_node(self, position):            
        current_node = self.head
        current_position = 0

        if position == 0:
            if self.head != None:
                self.head.next = None
                self.head = current_node.next
        else:
            while current_position < position:
                if current_node.next == None:
                    raise Exception('position too high')
                else:
                    current_node = current_node.next
                    current_position = current_position + 1
            temp = current_node.next
            current_node.next = temp.next
            temp.next = None
            return temp
