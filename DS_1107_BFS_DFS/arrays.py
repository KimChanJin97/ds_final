class Array:

    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.items = [None] * capacity

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item