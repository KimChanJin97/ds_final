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

class BSTree:
    def __init__(self, root):
        self.root = root

    def insert(self, elem):
        """using recursive insertion"""

        def insert_recursive(root):
            if root is None:
                return TreeNode(elem)
            if elem == root.elem:
                return root
            if elem < root.elem:
                root.left_child = insert_recursive(root.left_child)
            else:
                root.right_child = insert_recursive(root.right_child)

            return root

        self.root = insert_recursive(self.root)

    def traverse_preorder(self):
        ret = []

        def preorder_recursive(root):
            if root is None:
                return

            ret.append(root)
            preorder_recursive(root.left_child)
            preorder_recursive(root.right_child)

        preorder_recursive(self.root)
        return ret

    def search(self, elem):
        if self.root is None:
            raise Exception("the root is none")
        def search_recursive(root):
            if root is None: # root??? ???????????? ?????????
                return None # None ??????

            if elem == root.elem: # elem??? root ??? ???????????????
                return root # root ??????

            root = (
                search_recursive(root.left_child)
                if elem < root.elem # ?????? elem < root.elem ????????? ??????????????? root.left_child ??????
                else search_recursive(root.right_child)) # ?????? elem > root ????????? ??????????????? root.right_child ??????            )
            return root # ??? ????????? ??????

        return search_recursive(self.root) # search????????? serach_recursive(self.root) ????????? ??????

sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
root = BTreeBuilder.build(sexpr)
tree = BSTree(root)
actions = tree.traverse_preorder()
print(actions)
tree.insert(40)
actions = tree.traverse_preorder()
print(actions)
tree.insert(80)
actions = tree.traverse_preorder()
print(actions)
found = tree.search(40)
print(found.right_child)
print(found.left_child)