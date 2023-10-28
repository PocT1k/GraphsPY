import heapq as queueW

MaxNumberV = 1000000


#Дейкстры
def Deikstra(Graph1, Vlist, N, V0, Vend):
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
        distanse = weights[Vend]
        adjlist = []
        i = Vend
        if distanse == MaxNumberV:
            return 0, 0
        while i != V0:
            l = []
            l.append(p[i] + 1)
            l.append(i + 1)
            if Graph1.MD[i][p[i]] != 0 and Graph1.MD[i][p[i]] != 1:
                l.append(Graph1.MD[i][p[i]])
            i = p[i]
            adjlist.append(l)
        adjlist.reverse()
        return distanse, adjlist
pass

def spravka():
    print("**********************************************************************\n"
          "Автор работы: студент М3О-225Бк-21 Новиков К.А.\n"
          "Список ключей, доступных для ввода:\n"
          "    -e - ключ для ввода графа из файла, содержащего список ребер\n"
          "    -m - ключ для ввода графа из файла, содержащего матрицу смежности\n"
          "    -l - ключ для ввода графа из файла, содержащего список смежности\n"
          "Можно указать не более одного ключа для ввода графа!\n"
          "    -n begin_vertex_number обязательная задача начальной верщины\n"
          "    -d end_vertex_number обязательная задача конечной верщины\n"
          "    -o - ключ для вывода результатов работы программы в файл res.txt\n"
          "    -h - ключ для вывода справки\n"
          "**********************************************************************")
