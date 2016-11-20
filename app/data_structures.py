class Stack(object):
    """Implementation of Stack ADT"""

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue(object):
    """Implementation of Queue ADT."""

    def __init__(self, items=[]):
        self.items = items
        self.items.reverse()

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)


class Deque(object):
    """Implementation of Deque ADT."""

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Node(object):
    """Implementation of a Node."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class UnorderedList(object):
    """Implementation of unordered Linked list ADT."""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def append(self, item):
        self.add(item)

    def size(self):
        current = self.head
        counter = 0

        while current is not None:
            current = current.get_next()
            counter += 1

        return counter

    def search(self, item):
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous, current = current, current.get_next()

        if previous is None:
            if current is not None:
                self.head = current.get_next()
        else:
            if current is not None:
                previous.set_next(current.get_next())

    def insert(self, position, item):
        previous = None
        current = self.head
        found_pos = False
        counter = 0

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                previous, current = current, current.get_next()
                counter += 1

        if previous is None:
            self.add(item)
        else:
            node = Node(item)
            node.set_next(current)
            previous.set_next(node)

    def index(self, item):
        current = self.head
        found = False
        counter = 0

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                counter += 1

        if found:
            return counter

        raise ValueError('%s is not in the list' % item)

    def pop(self):
        if self.head:
            popped_data = self.head.get_data()
            self.head = self.head.get_next()

            return popped_data

    def __str__(self):
        items = ''

        current = self.head
        counter = 0

        while current:
            items += ', ' if len(items) > 1 else '['
            items += str(current.get_data())
            current = current.get_next()
            counter += 1

        if items:
            items += ']'
        else:
            items = 'None'

        return items
