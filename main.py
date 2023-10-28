import sys
from gr import *
from ut import *


#-e list_of_edges_t5_001.txt -n 1 -d 2
if __name__ == "__main__":
    input_string = input("Введите данные: ")
    array = input_string.split()
    array.insert(0, "1")

    if len(array) == 1 or ("-e" in array and "-l" in array) or ("-e" in array and "-m" in array) or (
            "-l" in array and "-m" in array):
        print(
            "Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in array:
        spravka()
        sys.exit(1)
    if "-n" not in array or "-d" not in array:
        print("Ошибка! Нужно указать ключи -n и -d для указания начальной и конечной вершины")
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
    Vend = int(array[array.index("-d") + 1]) - 1

    distance, adjlist = Deikstra(Graph1, Vlist, N, V0, Vend)
    if "-o" not in array:
        if distance == 0 and adjlist == 0:
            print(f"There is no path between the vertices {V0 + 1} and {Vend + 1}.")
        else:
            print(f"Shortest path length between {V0 + 1} and {Vend + 1} vertices: {distance}")
            print("Path:")
            print(adjlist)
    else:
        fout = open('res.txt', 'w')
        if distance == 0 and adjlist == 0:
            fout.write(f"There is no path between the vertices {V0 + 1} and {Vend + 1}.")
        else:
            fout.write(f"Shortest path length between {V0 + 1} and {Vend + 1} vertices: {distance}\n")
            fout.write("Path:\n")
            for i in adjlist:
                fout.write(str(i))
                fout.write(" ")
pass
