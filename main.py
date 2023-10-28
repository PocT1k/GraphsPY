import sys
from gr import *
from ut import *

#-e list_of_edges_t1_001.txt
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
    Vlist = []
    for i in range(N):
        l = []
        for j in range(N):
            if Graph1.MD[i][j] != 0:
                l.append(j)
        Vlist.append(l)
    V0 = list(range(0, N))
    V0.reverse()
    if Graph1.is_directed() == False:
        KompSV = BFS(Vlist, V0)
        if "-o" in array:
            fout = open('res.txt', 'w')
            if len(KompSV) == 1:
                fout.write("Graph is connected\n")
            else:
                fout.write("Graph is not connected\n")
            fout.write("The number of components: ", len(KompSV))
            fout.write(f"{KompSV}")
        else:
            if len(KompSV) == 1:
                print("Graph is connected")
            else:
                print("Graph is not connected")
            print("The number of components: ", len(KompSV))
            print(KompSV)
    else:
        MDTR = [0] * N
        MDST = [0] * N
        for i in range(N):
            MDTR[i] = [0] * N
            MDST[i] = [0] * N
        for i in range(N):
            for j in range(N):
                MDTR[i][j] = Graph1.MD[j][i]
                if Graph1.MD[i][j] != 0:
                    MDST[i][j] = 1
                    MDST[j][i] = 1
        Vlistreverse = []
        Vlistsoot = []
        for i in range(N):
            r = []
            l = []
            for j in range(N):
                if MDTR[i][j] != 0:
                    r.append(j)
                if MDST[i][j] != 0:
                    l.append(j)
            Vlistreverse.append(r)
            Vlistsoot.append(l)

        """Поиск компонент слабой связности"""
        KompSV = BFS(Vlistsoot, V0)
        if "-o" in array:
            fout = open('res.txt', 'w')
            if len(KompSV) == 1:
                fout.write("Graph is weakly connected\n")
            else:
                fout.write("The number of weakly connected components: ")
                fout.write(f"{len(KompSV)}")
            fout.write("\nConnected components: ")
            fout.write(f"{KompSV}")
        else:
            if len(KompSV) == 1:
                print("Graph is weakly connected")
            else:
                print("The number of weakly connected components: ")
                print(f"{len(KompSV)}")
            print("Connected components: ")
            print(f"{KompSV}")

        """Алгоритм Касараджу"""
        KompSV, Metki = DFS(Vlist, V0)
        i = 0
        while True:
            W = Metki.index(max(Metki))
            Metki[W] = -1
            V0[i] = W
            i += 1
            if i == N:
                break
        KompSV, Metki = DFS(Vlistreverse, V0)
        if "-o" in array:
            if len(KompSV) == 1:
                fout.write("Graph is strongly connected\n")
            else:
                fout.write("\nThe number of strongly connected components: ")
                fout.write(f"{len(KompSV)}")
            fout.write("\nStrongly connected components: \n")
            fout.write(f"{KompSV}")
        else:
            if len(KompSV) == 1:
                print("Graph is strongly connected")
            else:
                print("The number of strongly connected components: ", len(KompSV))
            print("Strongly connected components: ", KompSV)
