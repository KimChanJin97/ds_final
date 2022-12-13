class NodeEdge:
    def __init__(self, v1=None, v2=None):
        self.marked = False
        self.v1 = v1
        self.v2 = v2
        self.link_v1 = None
        self.link_v2 = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"({self.v1}:{self.v2})"


class GraphMultilistBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        ret = [None] * size
        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    continue

                if col <= row:
                    continue

                node = NodeEdge(v1=row, v2=col)
                node.link_v1 = ret[row]
                node.link_v2 = ret[col]
                ret[row] = node
                ret[col] = node

        return ret


class GraphMultiList:
    """Undirected graph"""

    def __init__(self, list_=None):
        self.list_ = list_

    def is_empty(self):
        return not self.list_

    def degree(self, v):
        sum_ = 0
        node = self.list_[v]
        while node is not None:
            sum_ += 1
            node = node.link_v1 if v == node.v1 else node.link_v2
        return sum_

    def explore(self, v):
        ret = []
        node = self.list_[v]
        while node is not None:
            ret.append(node)
            node = node.link_v1 if v == node.v1 else node.link_v2
        return ret

    def __len__(self):
        return len(self.list_)


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
    mat_ = read_input("input_g1.dat")
    print("Input matrix")
    print_mat(mat_)

    heads_ = GraphMultilistBuilder.build(mat_)
    graph = GraphMultiList(heads_)
    print()

    for i in range(len(graph)):
        path = graph.explore(i)
        print(f"vertex[{i}]: path = {path}")

    print()
    for i in range(len(graph)):
        degree = graph.degree(i)
        print(f"vertex[{i}]: degree = {degree}")
