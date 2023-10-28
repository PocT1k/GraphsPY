import sys
from gr import *
from ut import *


#-e list_of_edges_t3_001.txt
if __name__ == "__main__":
    input_string = input("Введите данные: ")
    array = input_string.split()
    array.insert(0, "1")

    if len(array) > 5 or len(array) == 1:
        print(
            "Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in array:
        spravka()
        sys.exit(1)
    fname = array[2]
    parametr = array[1]
    Graph1 = Graph(fname, parametr)
    N = Graph1.NumV

    SMD = [0] * N
    for i in range(N):
        SMD[i] = [0] * N
    for i in range(N):
        for j in range(N):
            if Graph1.MD[i][j] == 1:
                SMD[i][j] = 1
                SMD[j][i] = 1
    Vlist = []
    for i in range(N):
        l = []
        for j in range(N):
            if SMD[i][j] != 0:
                l.append(j)
        Vlist.append(l)

    visited = []
    time = 0
    V0list = list(range(0, N))
    V0 = V0list[0]
    tin = [0] * N
    tup = [0] * N
    Vobr = [-1] * N
    cutpoints = set()
    bridges = []


    def DFS(V0, p):
        global time
        visited.append(V0)
        n = 0
        time += 1
        tin[V0] = time
        tup[V0] = time
        for Vertex in Vlist[V0]:
            if Vertex == p:
                continue
            if Vertex not in visited:

                DFS(Vertex, V0)
                n += 1
                tup[V0] = min(tup[V0], tup[Vertex])
                if p != -1:
                    if tup[Vertex] >= tin[V0]:
                        cutpoints.add(V0 + 1)
                if tup[Vertex] > tin[V0]:
                    l = []
                    l.append(V0 + 1)
                    l.append(Vertex + 1)
                    l.sort()
                    bridges.append(l)
            else:
                tup[V0] = min(tup[V0], tin[Vertex])
        if p == -1 and n >= 2:  # корень и шарнир
            cutpoints.add(V0 + 1)


    """DFS"""
    for V in V0list:
        if V not in visited:
            DFS(V0, -1)
    print("Bridges: ")
    print(bridges)
    print("Cutpoints: ")
    for V in cutpoints:
        print(V, end=' ')
pass
