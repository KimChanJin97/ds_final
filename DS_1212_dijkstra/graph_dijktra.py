import math


class GraphDijkstra:
    def __init__(self, cost):
        self.cost = cost
        self.size = len(cost)

    def cal_dijkstra(self, v):
        visited = [False] * self.size
        dist, info = [math.inf] * self.size, [(math.inf, None)] * self.size

        visited[v], dist[v], info[v] = True, 0, (0, 0)
        u = 0
        print("init", f"{'-':>20}", "-", f"{str(dist):<30}", info)
        for i in range(self.size):
            u = self.choose(dist, visited, v)
            visited[u] = True

            for v in range(self.size):
                if (
                        self.cost[u][v] > 0
                        and not visited[v]
                        and dist[v] > dist[u] + self.cost[u][v]
                ):
                    dist[v] = dist[u] + self.cost[u][v]
                    info[v] = (dist[v], u)

            print(
                f"{i:4}",
                f"{str([j for j in range(len(visited)) if visited[j] == True]):>20}",
                u,
                f"{str(dist):<30}",
                info,
            )
        return dist, info

    def choose(self, dist, found, v):
        dist_min = math.inf  # infinity
        pos = v
        for i in range(self.size):
            if dist[i] < dist_min and not found[i]:
                dist_min = dist[i]
                pos = i
        return pos


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
    mat_ = read_input("input_00.dat")
    print("input matrix:")
    print_mat(mat_)

    graph = GraphDijkstra(mat_)
    v = 0
    print()
    print("info-table:")
    cost, path = graph.cal_dijkstra(v)

    print()
    print("dijkstra:")
    print("path:", [p for _, p in path])
    print("cost:", cost)