# 20180269 천성규
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        return self.items[-1]

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
        pos += 1

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class HeadNode:
    def __init__(self, id_=0, degree=0):
        self.id_ = id_
        self.degree = degree  # as indegree
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id_}"


class Node:
    def __init__(self, vertex=0, duration=0):
        self.vertex = vertex
        self.duration = duration
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.vertex, self.duration}"


class GraphAoeEstBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        ret = [HeadNode(i) for i in range(size)]

        for row in range(size):
            prev = ret[row]
            for col in range(size):
                if not mat[row][col]:
                    continue

                node = Node(col, mat[row][col])
                prev.link = node
                prev = node

        return ret


class GraphAoeEst:
    def __init__(self, list_, mat):
        self.list_ = list_
        self.mat = mat
        self.__build_indegree()

    def __build_indegree(self):
        for i, h in enumerate(self.list_):
            h.degree = self.indegree(i)

    def indegree(self, v):
        ret = 0
        for row in range(len(self.mat)):
            ret += bool(self.mat[row][v])
        return ret

    def outdegree(self, v):
        return sum(self.mat[v])

    def __getitem__(self, index):
        return self.list_[index]

    def __setitem__(self, index, value):
        self.list_[index] = value

    def __len__(self):
        return len(self.list_)

    def __str__(self):
        ret = ""
        for i, vt in enumerate(self):
            degree = vt.degree
            ret += f"v[{i}: {degree}] = "
            if vt is None or vt.link is None:
                ret += str(None) + "\n"
                continue

            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"

        return ret

    def cal_est(self):
        ret = [0] * len(self)
        self.__build_indegree()
        stack = Stack()
        # indegree 0 인 노드들을 stack 에 추가
        _ = [stack.push(v) for v in self.list_ if v.degree == 0]

        print(f"init\t{ret}\t{stack}")
        while not stack.is_empty():
            head = stack.peek()
            stack.pop()
            print(head, end="\t")
            d = ret[head.id_]
            node = head.link
            while node is not None:
                head = self[node.vertex]
                head.degree -= 1
                ret[head.id_] = max(node.duration + d, ret[head.id_])
                if head.degree == 0:
                    stack.push(head)
                node = node.link

            print(ret, end="\t")
            print(stack)  # stack 출력

        return ret


def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row,) = map(int, line.split())
            mat.append(row)
    return mat


def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    for row in range(rows):
        for col in range(cols):
            print(f"{mat[row][col]}", end=" ")
        print("\b")


if __name__ == "__main__":
    mat_ = read_input("input_aoe_00.dat")
    print("Input matrix:")
    print_mat(mat_)

    print()
    print("Adjacency list:")
    list_ = GraphAoeEstBuilder.build(mat_)
    graph = GraphAoeEst(list_, mat_)
    print(graph)

    print("earliest start time table:")
    est = graph.cal_est()

    print()
    print("EST:")
    print(est)