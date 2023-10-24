MaxNumberV = 1000


class Graph: #основной класс Графа
    def __init__(self, fname, par):
        NumV = 0 #n
        MD = [] #matrix
        if par == "-e":
            fin = open(fname, "r")
            Elist = []
            while True:
                line = fin.readline()
                line = list(map(int, line.split()))
                if not line:
                    break
                if (len(line) == 2):
                    line.append(1)
                Elist.append(line)
                if (line[0] > NumV or line[1] > NumV):
                    NumV = max(line[0], line[1])
            MD = [0] * NumV
            for i in range(NumV):
                MD[i] = [0] * NumV
            for k in range(len(Elist)):
                MD[(Elist[k][0]) - 1][(Elist[k][1]) - 1] = Elist[k][2];

        if par == "-m":
            fin = open(fname, "r")
            while (True):
                line = fin.readline().split()
                line = list(map(int, line))
                if not line:
                    break
                MD.append(line)
                NumV += 1

        if par == "-l":
            fin = open(fname, "r")
            Alist = []
            while (True):
                line = fin.readline().split()
                line = list(map(int, line))
                if not line:
                    break
                Alist.append(line)
                NumV += 1
            MD = [0] * NumV
            for i in range(NumV):
                MD[i] = [0] * NumV
            for i in range(NumV):
                for j in range(len(Alist[i])):
                    MD[i][Alist[i][j] - 1] = 1

        self.NumV = NumV
        self.MD = MD

    def weight(self, v1, v2):
        return self.MD[v1 - 1][v2 - 1]

    def is_edge(self, v1, v2):
        if self.MD[v1 - 1][v2 - 1] != 0:
            return True
        else:
            return False

    def adjacency_matrix(self):
        return self.MD

    def adjacenty_list(self, v):
        return self.MD[v - 1]

    def is_directed(self):
        for i in range(self.NumV):
            for j in range(i + 1, self.NumV):
                if self.MD[i][j] != self.MD[j][i]:
                    return True
        return False


pass


def spravka():
    print("**********************************************************************")
    print("Автор работы: студент М3О-325Бк-21 Новиков К.А. ")
    print("Список ключей, доступных для ввода: ")
    print("    -e - ключ для ввода графа из файла, содержащего список ребер ")
    print("    -m - ключ для ввода графа из файла, содержащего матрицу смежности")
    print("    -l - ключ для ввода графа из файла, содержащего список смежности ")
    print("Важно! Можно указать не более одного ключа для ввода графа!")
    print("    -o - ключ для вывода результатов работы программы в файл")
    print("    -h - ключ для вывода справки")
    print("**********************************************************************")


import sys

#python main.py -e list_of_edges_t1_001.txt

if __name__ == "__main__":
    if len(sys.argv) > 5 or len(sys.argv) == 1:
        print(
            "Ошибка! Нужно указать один из параметров -e, -m, -l, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)
    if "-h" in sys.argv:
        spravka()
        sys.exit(1)
    fname = sys.argv[2]
    parametr = sys.argv[1]

    Graph1 = Graph(fname, parametr)
    N = Graph1.NumV
    MDist = [0] * N
    for i in range(N):
        MDist[i] = Graph1.MD[i]

    for i in range(N):
        for j in range(N):
            if MDist[i][j] == 0:
                if i != j:
                    MDist[i][j] = MaxNumberV

    """Посчитать степени вершин"""
    if Graph1.is_directed() == False:
        deg = []
        for i in range(N):
            deg.append(sum(1 for i in MDist[i] if (i != MaxNumberV)) - 1)
    else:
        deg1 = [0] * N
        deg2 = [0] * N
        for i in range(N):
            for j in range(N):
                if MDist[i][j] != 0 and MDist[i][j] < MaxNumberV:
                    deg1[i] += 1
                    deg2[j] += 1

    """Алгоритм Флойда-Уоршелла"""
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if MDist[i][j] > MDist[i][k] + MDist[k][j]:
                    MDist[i][j] = MDist[i][k] + MDist[k][j]

    """Эксцентриситеты"""
    Exc = []
    P = []
    Z = []
    for i in range(N):
        MaxV = 0
        for j in range(N):
            if MDist[i][j] != MaxNumberV and MDist[i][j] > MaxV:
                MaxV = MDist[i][j]
        Exc.append(MaxV)
    D = max(Exc)
    R = min(Exc)
    for i in range(N):
        if Exc[i] == R: Z.append(i)
        if Exc[i] == D: P.append(i)

    if "-o" in sys.argv:
        fout = open('res.txt', 'w')
        if Graph1.is_directed() == False:
            fout.write("deg = ")
            fout.write(f"{deg}")
        else:
            fout.write(f"\ndeg(-) = , {deg1}")
            fout.write(f"\ndeg(+) = , {deg2}")
        fout.write("\nMatrix of Distences: \n")
        for i in range(N):
            for j in range(N):
                if MDist[i][j] == MaxNumberV:
                    fout.write("~ ")
                else:
                    fout.write(f"{MDist[i][j]:{3}}")
            fout.write("\n")
        fout.write("Eccentricity:\n")
        for i in range(N):
            fout.write(f"{Exc[i]} ")
        fout.write(f"\n D = {D}")
        fout.write(f"\n R = {R}")
        fout.write("\nCentral Virtex: ")
        for i in range(len(Z)):
            fout.write(f"{Z[i] + 1}")
        fout.write("\nPeriferal Virtex: ")
        for i in range(len(P)):
            fout.write(f"{P[i] + 1}")
    else:
        if Graph1.is_directed() == False:
            print("deg = ", deg)
        else:
            print("deg(-) = ", deg1)
            print("deg(+) = ", deg2)
        print("Matrix of Distences: ")
        for i in range(N):
            for j in range(N):
                if MDist[i][j] == MaxNumberV:
                    print("~", end=' ')
                else:
                    print(f'{MDist[i][j]:{3}}', end=' ')
            print()
        print("Eccentricity:")
        for i in range(N):
            print(Exc[i], end=' ')
        print()
        print(" D =", D, "\n", "R =", R)
        print("Central Virtex: ")
        for i in range(len(Z)):
            print(Z[i] + 1, end=' ')
        print()
        print("Periferal Virtex: ")
        for i in range(len(P)):
            print(P[i] + 1, end=' ')
