import sys
from gr import *
from ut import *


#python main.py -e list_of_edges_t1_001.txt
if __name__ == "__main__":
    # Ввод строки с клавиатуры
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

    if "-o" in array:
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
