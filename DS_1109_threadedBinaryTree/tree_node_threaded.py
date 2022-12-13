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

class BTreeBuilder:
    @staticmethod
    def build(sexpr):
        stack_proc = Stack()
        stack_subtree = Stack()
        root = None
        for expr in sexpr:
            if expr != ")":
                stack_proc.push(TreeNode(expr))
                continue

            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                node = node if node.elem != "#" else None
                stack_subtree.push(node)

            stack_proc.pop() # remove "("

            if stack_proc.is_empty():
                root = stack_subtree.peek()
                stack_subtree.pop()
            else:
                root = stack_proc.peek()
                stack_proc.pop()

            if stack_subtree.is_empty():
                continue

            root.left_child = stack_subtree.peek()
            stack_subtree.pop()
            root.right_child = stack_subtree.peek()
            stack_subtree.pop()
            stack_proc.push(root)

        if not stack_proc.is_empty():
            raise Exception("expression is wrong")

        return root

class TreeNodeThreaded:
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = self.right_child = None
        self.left_thread = self.right_thread = False
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.elem}"

class ThreadedBinaryTree:
    """Threaded Binary Tree"""
    def __init__(self, root=None):
        self.root = root
        self.head = TreeNodeThreaded()
        self.head.left_thread = True
        self.head.right_thread = False
        self.head.left_child = self.head
        self.head.right_child = self.head
        self.__build()
        # [H, D, I, B, E, A, F, C, G]
    def __build(self):
        """using inorder traversal"""
        root = self.root
        stack = Stack()
        actions = []
        # using inorder traversal
        raise NotImplemented
    def find_successor(self, root):
        node = None

        node = root
        while node and node.left_child:
            node = node.left_child

        return
def traverse_inorder(self):
        root = self.find_successor(self.head)
        ret = []
        while root is not None and root is not self.head: #
            ret.append(root)
            root = self.find_successor(root)
            return ret

if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root_ = BTreeBuilder.build(sexpr)
    tree = ThreadedBinaryTree(root_)
    root = tree.root
    e = root.left_child.right_child
    print(f"{e.left_child} <{e}> {e.right_child}") # B <E> A

    f = root.right_child.left_child
    print(f"{f.left_child} <{f}> {f.right_child}") # A <F> C

    g = root.right_child.right_child
    print(f"{g.left_child} <{g}> {g.right_child}") # C <G> None

    h = root.left_child.left_child.left_child
    print(f"{h.left_child} <{h}> {h.right_child}") # None <H> D

    i = root.left_child.left_child.right_child
    print(f"{i.left_child} <{i}> {i.right_child}") # D <I> B

    print()
    actions = tree.traverse_inorder()
    print(actions) # [H, D, I, B, E, A, F, C, G]

