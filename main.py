import sys
from gr import *
from ut import *


#-e list_of_edges_t6_001.txt -n 1 -t
if __name__ == "__main__":
    input_string = input("Введите данные: ")
    array = input_string.split()
    array.insert(0, "1")

    if len(array) == 1 or ("-e" in array and "-l" in array) or ("-e" in array and "-m" in array) or \
            ("-l" in array and "-m" in array):
        print("Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки. ")
        sys.exit(1)
    if ("-d" in array and "-b" in array) or ("-d" in array and "-t" in array) or \
            ("-b" in array and "-t" in array):
        print("Ошибка! Нужно указать один из параметров -d, -b, -t для рассчета. ")
    if "-h" in array:
        spravka()
        sys.exit(1)
    fname = array[2]
    parametr = array[1]
    Graph1 = Graph(fname, parametr)
    N = Graph1.NumV
    Vlist = []
    for i in range(N):
        m = []
        for j in range(N):
            if Graph1.MD[i][j] != 0:
                l = []
                l.append(j)
                l.append(Graph1.MD[i][j])
                m.append(l)
        Vlist.append(m)
    V0 = int(array[array.index("-n") + 1]) - 1
    if "-d" in array:
        if Graph1.negative_edges()==True:
            print("Алгоритм Дейкстры не допускает рёбра с отрицательным весом!")
            sys.exit(1)
        else:
            print("Graph does not contain edges with negative weight.")
            print(f"Shortest paths lengths from {V0 + 1}: ")
            print(Deikstra(V0, Vlist, N))
    if "-b" in array:
        print(BelmanFordMura(V0, Vlist, N))
    if "-t" in array:
        if BelmanFordMura(V0, Vlist, N) != "Graph contains negative weight cycle":
            print("Graph does not contain edges with negative weight.")
            print(f"Shortest paths lengths from {V0+1}: ")
            print(Levit(V0, Vlist, N))
        else:
            print("Graph contains negative weight cycle")
pass
