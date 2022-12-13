from stacks import Stack
from queues import Queue

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
        root = None

        # 메인 프로시저를 위한 스택
        stack_proc = Stack()
        # 서브트리를 위한 스택
        stack_subtree = Stack()

        for expr in sexpr:
            if expr != ")":
                stack_proc.push(TreeNode(expr))
                continue

            # case ")"
            # ( A ( B C
            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                # print(node)
                node = node if node.elem != "#" else None
                stack_subtree.push(node)

            # print(stack_subtree)

            stack_proc.pop()    # remove "("
            # print(stack_proc)
            # stack에 마지막 하나만(root) 들어가 있는 경우 ( A )
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

        # 기술한 sexpr 이 잘못되었을때 나오는 에러
        if not stack_proc.is_empty():
            raise Exception("expression is wrong.")

        return root


class BTree:
    def __init__(self, root):
        self.root = root

    def traverse_levelorder(self):

        ret = []
        ret.append(root)

        def postorder_recursive(root):
            if root.left_child is None:
                return
            ret.append(root.left_child)
            ret.append(root.right_child)
            postorder_recursive(root.left_child)

        postorder_recursive(self.root)
        return ret

    def traverse_levelorder_iterative(self):
        # using iterative
        ret = []
        root = self.root
        queue = Queue()
        right_queue = Queue
        ret.append(root)

        while not queue.is_empty() or root.left_child is not None:
            while root.left_child is not None:
                queue.enqueue(root.left_child)
                queue.enqueue(root.right_child)
                root = root.left_child

            node = queue.peek()
            queue.dequeue()
            ret.append(node)

        return ret

if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_levelorder()
    print(actions)

    actions = tree.traverse_levelorder_iterative()
    print(actions)