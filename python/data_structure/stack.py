class Stack:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def push(self, element):
        self.arr.append(element)

    def peek(self):
        return self.arr[len(self.arr)-1]

    def size(self):
        return len(self.arr)

    def pop(self):
        return self.arr.pop()
