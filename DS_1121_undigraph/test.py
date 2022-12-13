size = 4
graph = [[0] * size for _ in range(size)]
print(graph)

print("--------------------------------")
myList = [1,2,3,4,5]
aList = []
for i in myList:
    aList.append(i+1)
print(aList)

def add_one(n):
    return n + 1

result1 = map(add_one, myList) # map 객체 반환
print(result1)
result2 = list(map(add_one, myList)) # map 객체 반환한 것을 list로 형변환
print(result2)

print("--------------------------------")
myList1 = [[1,1,1],
          [2,2,2],
          [3,3,3],]
myList2 = [[4,4,4],
           [5,5,5],
           [6,6,6],]
*row1, sth1 = myList1
print(row1)
print(row1, sth1)

(*row2,) = myList2
print(row2)

print("--------------------------------")
tuple1 = (1,)
tuple2 = (1,2,3,4,5)
unpackedTuple1 = (*tuple1,)
unpackedTuple2 = (*tuple2,)
print(unpackedTuple1)
print(unpackedTuple2)

