import heapq as queueW

MaxNumberV = 1000000


#Дейкстры
def Deikstra(V0, Vlist, N):
    visited = set()
    weights = [MaxNumberV] * N
    weights[V0] = 0
    p = [None] * N
    queue = []
    queueW.heappush(queue, (0, V0))
    while queue:
        Vweigth, V = queueW.heappop(queue)
        visited.add(V)
        for U, Uweigth in Vlist[V]:
            if U not in visited:
                f = Vweigth + Uweigth
                if f < weights[U]:
                    weights[U] = f
                    p[U] = V
                    queueW.heappush(queue, (f, U))
    return weights

#Беллмана-Форма - МУра
def BelmanFordMura(V0, Vlist, N):
    weights = [MaxNumberV] * N
    weights[V0] = 0
    for i in range(N - 1):
        for j in range(len(Vlist)):
            for U, Uw in Vlist[j]:
                if weights[j] != MaxNumberV and weights[j] + Uw < weights[U]:
                    weights[U] = weights[j] + Uw
    for j in range(len(Vlist)):
        for U, Uw in Vlist[j]:
            if weights[j] != MaxNumberV and weights[j] + Uw < weights[U]:
                return "Graph contains negative weight cycle"
    print("Graph does not contain edges with negative weight.")
    print(f"Shortest paths lengths from {V0 + 1}: ")
    return weights

#Левита
def Levit(V0, Vlist, N):
    weights = [MaxNumberV] * N
    weights[V0] = 0
    M0 = []
    M1 = []
    M1.append(V0)
    M2 = []
    for V in range(N):
        if V != V0:
            M2.append(V)
    while M1:
        U = M1.pop()
        for V, Wuv in Vlist[U]:
            if V in M2:
                M1.append(V)
                M2.remove(V)
                weights[V] = min(weights[V], weights[U] + Wuv)
            elif V in M1:
                weights[V] = min(weights[V], weights[U] + Wuv)
            elif V in M0 and weights[V] > weights[U] + Wuv:
                M1.append(V)
                M0.remove(V)
                weights[V] = weights[U] + Wuv
        M0.append(U)
    return weights

def spravka():
    print("**********************************************************************\n"
          "Автор работы: студент М3О-225Бк-21 Новиков К.А.\n"
          "Список ключей, доступных для ввода:\n"
          "    -e - ключ для ввода графа из файла, содержащего список ребер\n"
          "    -m - ключ для ввода графа из файла, содержащего матрицу смежности\n"
          "    -l - ключ для ввода графа из файла, содержащего список смежности\n"
          "Можно указать не более одного ключа для ввода графа!\n"
          "    -d – алгоритм Дейкстры\n"
          "    -b – алгоритм Беллмана-Форда-Мура\n"
          "    -t – алгоритм Левита\n"
          "    -n begin_vertex_number - обязательный ключ начальной вершины\n"
          "    -o - ключ для вывода результатов работы программы в файл res.txt\n"
          "    -h - ключ для вывода справки\n"
          "**********************************************************************")
