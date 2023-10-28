MaxNumberV = 1000000


def Kruskala(Vlist, N, sootMD):
    visited = set()
    parent = [None] * N
    key = [MaxNumberV] * N
    key[0] = 0
    parent[0] = -1
    for _ in range(N):
        # Находим вершину с минимальным весом, которая еще не посещена
        min_key = MaxNumberV
        min_vertex = None
        for V in range(N):
            if V not in visited and key[V] < min_key:
                min_key = key[V]
                min_vertex = V
        visited.add(min_vertex)
        # Обновляем значения ключей и родительских вершин для смежных вершин
        for V in Vlist[min_vertex]:
            if V[0] not in visited and V[1]<key[V[0]]:
                key[V[0]] = V[1]
                parent[V[0]] = min_vertex

    # Собираем список ребер остовного дерева
    edges = []
    total_weight = 0
    for V in range(1, N):
        edges.append((parent[V]+1, V+1, sootMD[parent[V]][V]))
        total_weight += sootMD[parent[V]][V]
    return edges, total_weight

def Prima(Vlist, N, sootMD):
    visited = set()
    i = 0
    visited.add(0)
    total_weight = 0
    edges = []
    while (i < N - 1):
        minimum = MaxNumberV
        a = 0
        b = 0
        for V in range(N):
            if V in visited:
                for U, W in Vlist[V]:
                    if U not in visited:
                        if minimum > W:
                            minimum = W
                            a = V
                            b = U
        edges.append((a+1, b+1, sootMD[a][b]))
        total_weight += sootMD[a][b]
        visited.add(b)
        i += 1
    return edges, total_weight

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def Boruvka(Vlist, N, sootMD):
    parent = []
    rank = []
    edges = []
    cheapest = []
    numC = N
    total_weight = 0
    for node in range(N):
        parent.append(node)
        rank.append(0)
        cheapest = [-1] * N
    while numC > 1:
        for u in range(len(Vlist)):
            for v, w in Vlist[u]:
                set1 = find(parent, u)
                set2 = find(parent, v)
                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]
        for node in range(N):
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                set1 = find(parent, u)
                set2 = find(parent, v)
                if set1 != set2:
                    total_weight += w
                    union(parent, rank, set1, set2)
                    print((u+1, v+1, w))
                    edges.append((u+1, v+1, w))
        numC = numC - 1
        cheapest = [-1] * N
    return edges, total_weight

def spravka():
    print("**********************************************************************\n"
          "Автор работы: студент М3О-225Бк-21 Новиков К.А.\n"
          "Список ключей, доступных для ввода:\n"
          "    -e - ключ для ввода графа из файла, содержащего список ребер\n"
          "    -m - ключ для ввода графа из файла, содержащего матрицу смежности\n"
          "    -l - ключ для ввода графа из файла, содержащего список смежности\n"
          "Можно указать не более одного ключа для ввода графа!\n"
          "    -k – алгоритм Крускала\n"
          "    -p – алгоритм Прима\n"
          "    -b – алгоритм Борувки\n"
          "    -s – расчёт производится тремя алгоритмами поочерёдно\n"
          "    -o - ключ для вывода результатов работы программы в файл res.txt\n"
          "    -h - ключ для вывода справки\n"
          "**********************************************************************")
