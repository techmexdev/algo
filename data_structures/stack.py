class Stack:
    def __init__(self):
        pass

    def push(self, item):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def isEmpty(self):
        pass

class ArrayStack(Stack):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

class LinkedListStack(Stack):
    def __init__(self):
        pass

    def push(self, item):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def isEmpty(self):
        pass