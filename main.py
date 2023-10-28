import sys
import timeit
from gr import *
from ut import *


#-e list_of_edges_t4_001.txt -s
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
    sootMD = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Graph1.MD[i][j]!=0:
                sootMD[i][j] = Graph1.MD[i][j]
                sootMD[j][i] = Graph1.MD[i][j]

    Vlist = []
    for i in range(N):
        m=[]
        for j in range(N):
            if sootMD[i][j] != 0:
                l = []
                l.append(j)
                l.append(sootMD[i][j])
                m.append(l)
        Vlist.append(m)
    if "-k" in array:
        print(Kruskala(Vlist, N, sootMD))
        sys.exit(1)
    if "-p" in array:
        print(Prima(Vlist, N, sootMD))
        sys.exit(1)
    if "-b" in array:
        print(Boruvka(Vlist, N, sootMD))
        sys.exit(1)
    if "-s" in array:
        st = timeit.default_timer()
        ed, tw = Kruskala(Vlist, N, sootMD)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
        st = timeit.default_timer()
        ed, tw = Prima(Vlist, N, sootMD)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
        st = timeit.default_timer()
        ed, tw = Boruvka(Vlist, N, sootMD)
        time = timeit.default_timer() - st
        print(ed, tw)
        print(f"{time:.04f}")
