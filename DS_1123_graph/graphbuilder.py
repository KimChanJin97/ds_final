class UndiGraph:
    def __build(self):
        size = len(mat)
        for row in range(size):
            prev = self.list_[row]
            for col in range(size):
                if not self.mat[row][col]:
                    continue
                node = Node(col)

    if prev is None:
        self.list_[row] = node
    else:
        prev.link = node
    prev = node

    def __init__(self, size):
        self.graph = [[0] * size for _ in range(size)]


    def insert_edge(self, src, dst, elem=1): # 간선이 존재함을 1로 표현
        self.graph[src][dst] = self.graph[dst][src] = elem


    def remove_edge(self, src, dst, elem=0):
        self.graph[src][dst] = self.graph[dst][src] = elem


    def degree(self, v):
        return sum(self.graph[v])


    def __getitem__(self, coords): # 행렬의 1 대신 값을 넣음으로써 꼭짓점 값 표현
        x, y = coords
        return self.graph[x][y]


    def __setitem__(self, coords, elem):
        x, y = coords
        self.graph[x][y] = elem


    def __len__(self):
        return len(self.graph)


    def __str__(self):
        ret = ""
        for row in range(len(self.graph)):
            ret += str(self.graph[row]) + "\n"
        return ret.strip()

class GraphBuilder:
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
            node = Node(col)
            node.link = ret[row]
            ret[row] = node

        return ret
