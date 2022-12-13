class UndiGraph:


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



if __name__ == "__main__":
    VERTICES = 4
    graph = UndiGraph(VERTICES)
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 3)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 3)
    print("graph")

    for row in range(len(graph)):
        for col in range(len(graph)):
            print(graph[row, col], end=" ")
        print()

    print()
    v = 0
    print(f"degree[{v}] = {graph.degree(v)}")
    v = 3
    print(f"degree[{v}] = {graph.degree(v)}")

    print()
    print("graph")
    print(graph)