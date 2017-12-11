class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found = None

        while current != None and not found:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()

        return found

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def remove(sef, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item
                found = True
                break
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self):

    def index(item):

    def insert(self, pos, item):

    def pop(self):

    def pop(self, pos):
