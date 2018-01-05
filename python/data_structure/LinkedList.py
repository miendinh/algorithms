class Node:
    def __init__(self, value, prev = None, next_ = None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove(self, value):
        node = self.search(value)
        if not node:
            return False

        if self.head == node:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        return True

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            else:
                current = current.next
        return None

head = Node(1)
ll = LinkedList(head)

for i in range(2, 101):
    ll.append(i)

assert(ll.search(50).value == 50)
assert(ll.remove(50) == True)
assert(ll.search(50) == None)

assert(ll.search(1).value == 1)
assert(ll.remove(1) == True)
assert(ll.search(1) == None)

assert(ll.search(100).value == 100)
assert(ll.remove(100) == True)
assert(ll.search(100) == None)
