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

    def delete(self, elem):

        def delete_recursive(root):
            if root is None: # root가 None 이라면
                return root # root 리턴하고 종료

            # root에서 출발하여 삭제할 것(=elem)을 찾아 떠나는 여정
            if elem < root.elem: # 만약 elem(=삭제할 node) < root.elem(root node) 이라면
                root.left_child = delete_recursive(root.left_child)
                # 재귀적으로 delete_recursive(root.left_child) 한 결과값을 root.left_child 대입
            elif elem > root.elem: # 만약 elem(=삭제할 node) > root.elem(root node) 이라면
                root.right_child = delete_recursive(root.right_child)
                # 재귀적으로 delete_recursive(root.right_child) 한 결과값을 root.right_child 대입
            else: # 만약 elem(=삭제할 node) == root.elem 이라면, 즉 삭제할 node를 찾았다면
                if root.left_child is None: # 만약 root.left_child가 None 이라면
                    temp = root.right_child # temp에 root.right_child 담고
                    root = None # root는 None으로 바꾸고
                    return temp # temp(=root.right_child) 리턴
                elif root.right_child is None: # 만약 root.right_child가 None 이라면
                    temp = root.left_child # temp에 root.right_child 담고
                    root = None # root는 None으로 바꾸고
                    return temp # temp(=root.left_child) 리턴

                # 전략 : 오른쪽(big) -> 왼쪽(small), 왼쪽(small)을 삭제한 node 대체
                # 현재 root.elem 은 elem(=삭제할 node)임

                # 오른쪽(big)
                current = root.right_child # current에 root.right_child 담고
                temp_root = root # temp_root에 root 담는다

                # 왼쪽(small)
                # while문 쓰는 이유는 degree 0 또는 1 인 leaf node로 삭제할 node를 대체하기 위함임
                while current.left_child is not None: # current.left_child가 None이 아닌 동안
                    current = current.left_child # current에 current.left_child 대입

                temp = current # temp에 current 대입
                temp_root.elem = temp.elem # temp_root.elem (=root.elem)에 temp.elem 대입

                temp_root.right_child = delete_recursive(temp_root.elem)

            return

sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
root = BTreeBuilder.build(sexpr)
tree = BSTree(root)
actions = tree.traverse_preorder()
print(actions)
tree.delete(40)
