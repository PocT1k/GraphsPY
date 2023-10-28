import sys
from gr import *
from ut import *


#-e list_of_edges_t7_001.txt
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

    D = Djonson(Vlist, N)
    if D == None:
        if "-o" in array:
            fout = open('res.txt', 'w')
            fout.write("Graph contains negative weight cycle")
        else:
            print("Graph contains negative weight cycle")
    else:
        if "-o" in array:
            fout = open('res.txt', 'w')
            if Graph1.negative_edges()==True:
                fout.write("Graph contains edges with negative weight.\n")
            else:
                fout.write("Graph doesn't contain edges with negative weight.\n")
            fout.write("Shortest paths lengths:\n")
            for i in range(len(D)):
                for j in range(len(D[i])):
                    if i != j and D[i][j] != MaxNumberV:
                        fout.write(f"{i+1} - {j+1}: {D[i][j]}\n")
        else:
            if Graph1.negative_edges()==True:
                print("Graph contains edges with negative weight.")
            else:
                print("Graph doesn't contain edges with negative weight.")
            print("Shortest paths lengths:")
            for i in range(len(D)):
                for j in range(len(D[i])):
                    if i != j and D[i][j] != MaxNumberV:
                        print(f"{i+1} - {j+1}: {D[i][j]}")
pass
