from linked_list import LinkedList

class ArrayStack:
    top = 0
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None for x in range(max_size)]

    def push(self, item):
        if self.top == self.max_size:
            raise Exception('stack overflow')
        else:
            self.items[self.top] = item
            self.top += 1

    def pop(self):
        if self.top == 0:
            raise Exception('min number of items reached')
        else:
            self.items[self.top] = None
            self.top -= 1

    def peek(self):
        if self.top > 0:
            return self.items[self.top]
        else:
            return None

    def isEmpty(self):
        return self.top == 0

class LinkedListStack(LinkedList):
    def push(self, item):
        self.append_node_right(item)

    def pop(self):
        return self.delete_node_right(item)
        
    def peek(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        return current_node

    def isEmpty(self):
        return self.head == None