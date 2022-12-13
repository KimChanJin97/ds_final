# 예제 1
"""
def init_set(len):
    return [-1] * len

def union(parent, i, j):
    parent[i] = j

def find(parent, i):
    while parent[i] >= 0:
        i = parent[i]
    return i

if __name__ == "__main__":
    p = init_set(10)

    # S1
    union(p, 6, 0)
    union(p, 7, 0)
    union(p, 8, 0)

    # S2
    union(p, 1, 4)
    union(p, 9, 4)

    # S3
    union(p, 3, 2)
    union(p, 5, 2)

    print()
    print("sets:")
    print(p)
"""



# 예제 2
"""
def init_set(len):
    return [-1] * len

def union(parent, i, j):
    parent[i] = j

def find(parent, i):
    while parent[i] >= 0:
        i = parent[i]
    return i

if __name__ == "__main__":
    p = init_set(10)

    #Union
    union(p, 0, 1)
    union(p, 1, 2)
    union(p, 2, 3)
    union(p, 3, 4)
    union(p, 4, 5)
    union(p, 5, 6)
    union(p, 6, 7)
    union(p, 7, 8)
    union(p, 8, 9)

    for i in range(9):
        union(p, i, i+1)

    print()
    print("sets:")
    print(p)
"""



# 예제 3 : 큰 쪽에 달기
"""
def init_set(len):
    return [-1] * len, [-1] * len

def uinion(parent, count,i, j):
    temp = parent[i] + parent[j]
    if parent[i] > parent[j]:
        parent[i] =j
        parent[j] = temp
    else:
        parent[j] = i
        parent[i] = temp

def find(parent, i):
    while parent[i] >= 0:
        i = parent[i]
    return i

if __name__ == "__main__":
    parent, count = init_set(10)
    uinion(parent, count, 0, 1)
    uinion(parent, count, 0, 2)
    uinion(parent, count, 0, 3)
    uinion(parent, count, 0, 4)
    uinion(parent, count, 0, 5)
    uinion(parent, count, 0, 6)
    uinion(parent, count, 0, 7)
    uinion(parent, count, 0, 8)
    uinion(parent, count, 0, 9)
    print(parent)
"""