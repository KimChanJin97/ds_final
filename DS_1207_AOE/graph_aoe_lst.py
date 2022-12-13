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
        self.degree = degree # as indegree
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id_}"



class Node:
    def __init__(self, vertex=0, duration=0):
        self.vertex = vertex
        self.link = None
        self.duration = duration

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.vertex, self.duration}"



class GraphAoeLstBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        list_ = [HeadNode(i) for i in range(size)]

        for row in range(size):
            prev = list_[row]
            for col in range(size):
                if not mat[row][col]:
                    continue

                node = Node(col)
                prev.link = node
                prev = node

        return list_


class GraphAoeLst:
    def __init__(self, mat, list_, est):
        self.list_ = list_  # inverse adjacency list
        self.est = est
        self.mat = mat
        self.build_outdegree()

    def build_outdegree(self):
        for i, h in enumerate(self.list_):
            h.degree = self.outdegree(i)

    def outdegree(self, v):
        ret = len([i for i in self.mat[v] if i != 0])
        return ret

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

            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret

    def cal_lst(self):
        ret = [max(self.est)] * len(self)
        self.build_outdegree()

        stack = Stack()
        # topology sort
        _ = [stack.push(v) for v in self.list_ if v.degree == 0]

        print(f"init\t{ret}\t{stack}")
        while not stack.is_empty():
            # print(stack)
            head = stack.peek()
            stack.pop()
            print(head, end="\t")

            d = ret[head.id_]
            node = head.link

            while node is not None:
                head = self[node.vertex]
                head.degree -= 1
                ret[head.id_] = min(d - node.duration, ret[head.id_])

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
    print("EST:")
    (*est,) = 0, 6, 4, 5, 7, 7, 16, 14, 18
    print(est)
    list_ = GraphAoeLstBuilder.build(mat_)
    graph = GraphAoeLst(mat_, list_, est)
    print()
    print("Inverse Adjacency list:")
    print(graph)
    print("Latest start time table:")
    lst = graph.cal_lst()
    print(lst)
