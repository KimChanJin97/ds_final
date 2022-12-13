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
        parent = None
        root = self.root

        while root is not None and elem != root.elem: # root가 None이 아니고 elem이 root.elem과 동일하지 않는 동안
            parent = root # parent에 root 대입
            root = root.left_child if elem < root.elem else root.right_child
            # 만약 elem < root.elem 이라면 root에 root.left_child 대입
            # 만약 elem > root.elem 이라면 root에 root.right_child 대입

        # root가 None이고 elem이 root.elem과 동일한 동안
        if root is not None: # root가 None이 아니라면 종료
            return

        # root 존재한다면
        node_new = TreeNode(elem) # elem을 TreeNode에 넣어서 node_new 생성
        if parent is None: # parent가 뭐지?
            self.root = node_new
            return

        if parent.elem > node_new.elem: #
            parent.left_child = node_new #
        else: #
            parent.right_child = node_new #

        # 새로운 노드를 하나 만들어서 넣는다.
        # 내가 왼쪽에 넣을지 오른쪽일지 모르는데 그러면 parent의 키값과 비교해서 root가 더 크면
        # 루트의 좌측에 짚어넣는다. 그렇지 않으면 우측에 넣으면 된다.

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
            if root is None: # root가 존재하지 않다면
                return None # None 리턴

            if elem == root.elem: # elem이 root 와 동일하다면
                return root # root 리턴

            root = (
                search_recursive(root.left_child)
                if elem < root.elem # 만약 elem < root.elem 이라면 재귀적으로 root.left_child 탐색
                else search_recursive(root.right_child)) # 만약 elem > root 이라면 재귀적으로 root.right_child 탐색            )
            return root # 그 결과값 리턴

        return search_recursive(self.root) # search함수는 serach_recursive(self.root) 결과값 리턴

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
