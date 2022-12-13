class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
        pos += 1

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    print("Len:", len(queue))
    print("Is Empty:", queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    print("Len:", len(queue), queue)
    print("Is Empty:", queue.is_empty())
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Len:", len(queue), queue)
    print()
    N = 5
    for i in range(1, N + 1):
        queue.enqueue(i)
        print("Len:", len(queue), queue)

    while not queue.is_empty():
        print("Peek:", queue.peek(), "Len:", len(queue), queue)
        queue.dequeue()
    print("Len:", len(queue), queue)

'''
Len: 0
Is Empty: True
[2, 1]
Len: 2 [2, 1]
Is Empty: False
Peek: 1
Peek: 2
Len: 0 []

Len: 1 [1]
Len: 2 [2, 1]
Len: 3 [3, 2, 1]
Len: 4 [4, 3, 2, 1]
Len: 5 [5, 4, 3, 2, 1]
Peek: 1 Len: 5 [5, 4, 3, 2, 1]
Peek: 2 Len: 4 [5, 4, 3, 2]
Peek: 3 Len: 3 [5, 4, 3]
Peek: 4 Len: 2 [5, 4]
Peek: 5 Len: 1 [5]
Len: 0 []
'''