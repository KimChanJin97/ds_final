from arrays import Array

class Stack:
    CAPACITY = 15

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.top = -1

    def is_full(self):
        return self.top >= self.capacity

    def is_empty(self):
        return self.top < 0

    def push(self, elem):
        if self.is_full():
            raise Exception("stack is full.")

        self.top += 1
        self.arr[self.top] = elem

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")

        self.arr[self.top] = None
        # self.arr[len(self) - 1] = None
        self.top -= 1

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")

        # return self.arr[len(self) - 1]
        return self.arr[self.top]

    def __len__(self):
        return self.top + 1

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)