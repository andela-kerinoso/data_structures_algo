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


class OrderedList(object):
    """Implementation of ordered Linked list."""

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        previous = None
        current = self.head
        found = False

        while current and not found:
            if current.get_data() < item:
                found = True
            else:
                previous, current = current, current.get_next()

        node = Node(item)
        node.set_next(current)
        self.length += 1

        if previous is None:
            self.head = node
        else:
            previous.set_next(node)

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

        while current and current.get_data() >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current and current.get_data() >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                previous, current = current, current.get_next()

        if previous is None:
            if found and current is not None:
                self.head = current.get_next()
                self.length -= 1
        else:
            if found and current is not None:
                previous.set_next(current.get_next())
                self.length -= 1

    def retrieve(self, position):
        current = self.head
        found_pos = False
        counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                current = current.get_next()
                counter -= 1

        if found_pos:
            return current.get_data()

        raise ValueError('Index %s is out of bound.' % position)

    def index(self, item):
        current = self.head
        found = False
        counter = self.length - 1

        while current and current.get_data >= item and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                counter -= 1

        if found:
            return counter

        raise ValueError('%s is not in the list' % item)

    def pop(self, position=None):
        previous = None
        current = self.head
        found_pos = True

        if position is not None:
            found_pos = False
            counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                previous, current = current, current.get_next()
                counter -= 1

        if previous is None:
            if current is not None:
                popped_data = current.get_data()
                self.head = current.get_next()
        else:
            if current is not None:
                popped_data = current.get_data()
                previous.set_next(current.get_next())

        if current:
            self.length -= 1
            return popped_data

        raise ValueError('Index %s is out of bound.' % position if position else 'List is empty.')

    def __getitem__(self, position):
        return self.retrieve(position)

    def __str__(self):
        items = ''

        current = self.head
        counter = 0

        while current:
            if not items:
                items = ']'

            items = str(current.get_data()) + items
            current = current.get_next()

            if current:
                items = ', ' + items

            counter += 1

        if items:
            items = '[' + items
        else:
            items = '[]'

        return items


class UnorderedList(OrderedList):
    """Implementation of unordered Linked list ADT."""

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def append(self, item):
        self.add(item)

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
                self.length -= 1
        else:
            if current is not None:
                previous.set_next(current.get_next())
                self.length -= 1

    def insert(self, position, item):
        previous = None
        current = self.head
        found_pos = False
        counter = self.length - 1

        while current and not found_pos:
            if counter == position:
                found_pos = True
            else:
                previous, current = current, current.get_next()
                counter -= 1

        if previous is None:
            self.add(item)
        else:
            node = Node(item)
            node.set_next(current)
            previous.set_next(node)
            self.length += 1

    def index(self, item):
        current = self.head
        found = False
        counter = self.length - 1

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                counter -= 1

        if found:
            return counter

        raise ValueError('%s is not in the list' % item)

    def __setitem__(self, position, item):
        self.insert(position, item)


class Map(object):
    """Implementation of Map ADT."""

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, table_size):
        total = 0

        for pos in range(len(key)):
            total += ord(key[pos]) * (pos + 1)

        return total % table_size

    @staticmethod
    def rehash_function(old_hash, table_size):
        return (old_hash + 1) % table_size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            hash_value = self.rehash_function(hash_value, self.size)
            while self.slots[hash_value] is not None and self.slots[hash_value] != key:
                hash_value = self.rehash_function(hash_value, self.size)

            if self.slots[hash_value] is None:
                self.slots[hash_value] = key
                self.data[hash_value] = data
            else:
                self.data[hash_value] = data

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        found = stop = False
        start_hash_value = hash_value

        while self.slots[hash_value] is not None and not (found or stop):
            if self.slots[hash_value] == key:
                found = True
            else:
                hash_value = self.rehash_function(hash_value, self.size)
                if hash_value == start_hash_value:
                    stop = True

        return self.data[hash_value]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
