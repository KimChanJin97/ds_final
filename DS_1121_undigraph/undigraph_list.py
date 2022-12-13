class Node:


    def __init__(self, item=None):
        self.item = item
        self.link = None


    def __str__(self):
        return f"{self.item}"



class UndiGraph:


    def __init__(self, mat):
        self.mat = mat # 매트릭스
        self.vertices = len(mat) # 행
        self.linked = [None] * self.vertices #
        self.__build()


    def __build(self):
        size = len(mat) # 행 길이
        for r in range(size): # 행 길이
            for c in range(size): # 열 길이(=행 길이)
                if not self.mat[r][c]: # 매트릭스 원소가 0이라면
                    continue
                self.add_edge(r, c)


    def add_edge(self, src, dst):
        if self.linked[src] is None:
            self.linked[src] = Node(dst)
            return

        prev = vt = self.linked[src]
        while vt is not None:
            prev, vt = vt, vt.link

        prev.link = Node(dst)


    def __str__(self):
        ret = ""
        for i, vt in enumerate(self.linked):
            ret += f"v[{i}] = "
            if vt is None:
                ret += "None\n"
                continue
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret

# 0 1 1 0 0 0 0 0
# 1 0 0 1 0 0 0 0
# 1 0 0 1 0 0 0 0
# 0 1 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 1 0 1 0
# 0 0 0 0 0 1 0 1
# 0 0 0 0 0 0 1 0

def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f: # 파일 읽기
        for line in f: # 한 줄씩
            # tuple unpacking
            (*row,) = map(int, line.split()) # 한 글자씩 정수형으로 변환하고 tuple unpacking
            mat.append(row)
    return mat

# [
#  (0, 1, 1, 0, 0, 0, 0, 0,),
#  (1, 0, 0, 1, 0, 0, 0, 0,),
#  (1, 0, 0, 1, 0, 0, 0, 0,),
#  (0, 1, 1, 0, 0, 0, 0, 0,),
#  (0, 0, 0, 0, 0, 1, 0, 0,),
#  (0, 0, 0, 0, 1, 0, 1, 0,),
#  (0, 0, 0, 0, 0, 1, 0, 1,),
#  (0, 0, 0, 0, 0, 0, 1, 0,),
# ]


def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    print("Input matrix is")
    for row in range(rows): # 행
        for col in range(cols): # 열
            print(f"{mat[row][col]}", end=" ")
        print("\b") # 각 튜플의 마지막 원소 뒤 공백 지우고 줄바꿈



if __name__ == "__main__":
    mat = read_input("input_g4.dat")
    print_mat(mat)

    print()
    print("Adjacency list is")
    graph = UndiGraph(mat)
    print(graph)