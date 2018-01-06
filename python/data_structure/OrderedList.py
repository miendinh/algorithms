import random

class Node:
    def __init__(self, value, prev = None, next_ = None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        return self.value

class OrderedList:

    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            prev    = None
            while current and current.value >= value:
                prev = current
                current = current.next

            if prev:
                prev.next = node
                node.prev = prev
            else:
                self.head = node
                node.next = prev

            if current:
                current.prev = node
                node.next = current

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

# Test
ol = OrderedList()
l = list(range(100))
l = random.sample(l, len(l))

for i in l:
    ol.append(i)

assert(str(ol) == str(list(reversed(sorted(l)))))
