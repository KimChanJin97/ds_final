# btree.py
# Using stack
# ( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )

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

class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.elem}"

class BTree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        it = iter(sexpr)

        root = None
        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            if token != ")":
                if token == "(" and not stack.is_empty():
                    root = stack.peek()
                if token == "#":
                    stack.push(TreeNode(None))
                else:
                    stack.push(TreeNode(token))
                continue

            prev = None

            while stack.peek().elem != "(":
                node = stack.peek() #
                stack.pop()
                checker = 0
                if root == node:
                    a = stack.peek()
                    stack.pop()
                    if not stack.is_empty():
                        b = stack.peek()
                        stack.pop()
                        root = stack.peek()
                        stack.push(b)
                        stack.push(a)
                    else:
                        stack.push(a)
                        checker += 1

                if checker == 0:
                    if root.right_child is None:
                        root.right_child = node
                    else:
                        root.left_child = node

                prev = node

            stack.pop()

            if stack.is_empty():
                root = prev
                continue

            root = stack.peek()

            root.left_child = prev

            stack.pop()
            stack.push(root)

        if not stack.is_empty():
            raise Exception("expression is wrong.")

        self.root = root


if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
    tree = BTree()
    tree.build(sexpr)

    print(tree.root)
    print(tree.root.left_child)
    print(tree.root.left_child.left_child)
    print(tree.root.left_child.right_child)
    print(tree.root.right_child)
    print(tree.root.right_child.left_child)
    print(tree.root.right_child.right_child)

"""
30 
5
2 
None 
40 
None 
80
"""