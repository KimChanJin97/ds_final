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
    def __init__(self, root):
        self.root = root

    def traverse_inorder(self):
        ret=[]

        def inorder_recursive(root):
            if root is None: # root가 None이라면
                return # 재귀함수 탈출

            # root에 뭔가가 있다면
            inorder_recursive(root.left_child) # L
            # 재귀함수 인자로 root의 왼쪽노드
            ret.append(root) # V
            # L이 None 임을 알고 V(root)로 돌아와서 이를 append
            inorder_recursive(root.right_child) # R
            # 재귀함수 인자로 root의 오른쪽노드

        inorder_recursive(self.root)
        return ret

    def traverse_preorder(self):
        ret=[]

        def preorder_recursive(root):
            if root is None:
                return

            ret.append(root)  # V
            preorder_recursive(root.left_child) # L
            preorder_recursive(root.right_child) # R

        preorder_recursive(self.root)
        return ret

    def traverse_postorder(self):
        ret=[]

        def postorder_recursive(root):
            if root is None:
                return

            postorder_recursive(root.left_child) # L
            postorder_recursive(root.right_child) # R
            ret.append(root)  # V

        postorder_recursive(self.root)
        return ret

    def traverse_inorder_iterative(self):
        ret = []
        root = self.root
        stack = Stack()

        while not stack.is_empty() or root is not None:
            # 빈트리가 아니라면, 빈스택이 아니라면 (둘 중 하나라도 참이면 참)
            while root is not None: # None이 나올 때까지
                stack.push(root) # 스택에 push
                root = root.left_child # 새root는 전root의 왼쪽노드로 대입

            node = stack.peek()
            stack.pop()
            ret.append(node)

            root = node.right_child

        return ret

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

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)

    actions_inorder = tree.traverse_inorder()
    actions_preorder = tree.traverse_preorder()
    actions_postorder = tree.traverse_postorder()
    actions_inorder_iterative = tree.traverse_inorder_iterative()

    print(actions_inorder)
    print(actions_preorder)
    print(actions_postorder)
    print(actions_inorder_iterative)

    sexpr1 = "( A ( B ( D ( G H ) ) C ( E ( # I ) F ) )".split()
    root1 = BTreeBuilder.build(sexpr1)
    tree1 = BTree(root1)

    quiz_inorder = tree1.traverse_inorder()

    print(quiz_inorder)

# ------
# 빈트리가 아니라면
# 빈스택이 아니라면
# 둘 중에 하나라도 참이면 참

# None 나올 때까지
# 좌하단으로 쭉 내려감
# None 전까지 push

# 해결했으니 A pop
# root에 A 의 right_child로 대입
# ------
# A의 right_child를 root로 삼고 다시 반복문 수행
# ------
# 빈트리가 아니라면
# 빈스택이 아니라면
# 둘 중에 하나라도 참이면 참

# None이 나올 때까지
# 좌하단으로 쭉 내려감
# None 전까지 push

# 해결했으니
