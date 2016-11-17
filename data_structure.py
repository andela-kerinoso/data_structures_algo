class Stack(object):
    """Implementation of Stack ADT"""

    def __init__(self, items):
        self.items = items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.appends(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
