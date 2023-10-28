import heapq as queueW

MaxNumberV = 1000


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
        for U, Uw in Vlist[V]:
            if U not in visited:
                f = Vweigth + Uw
                if f < weights[U]:
                    weights[U] = f
                    p[U] = V
                    queueW.heappush(queue, (f, U))
    return weights

#Беллмана-Форда
def BelmanFordMura(V0, Vlist):
    weights = [MaxNumberV] * len(Vlist)
    weights[V0] = 0
    for _ in range(len(Vlist) - 1):
        for j in range(len(Vlist)):
            for U, Uw in Vlist[j]:
                if weights[j] + Uw < weights[U]:
                    weights[U] = weights[j] + Uw
    for j in range(len(Vlist)):
        for U, Uw in Vlist[j]:
            if weights[j] != MaxNumberV and weights[j] + Uw < weights[U]:
                return None
    return weights

#Джонсона
def Djonson(Vlist, N):
    m=[]
    for i in range(N):
        l = []
        l.append(i)
        l.append(0)
        m.append(l)
    Vlist.append(m)
    q = len(Vlist)-1
    h = BelmanFordMura(q, Vlist)
    if h == None:
        return None
    Vlist2=[]
    for U in range(len(Vlist)-1):
        m=[]
        for V, W in Vlist[U]:
            W2 = W + h[U] - h[V]
            l=[]
            l.append(V)
            l.append(W2)
            m.append(l)
        Vlist2.append(m)
    distance = []
    for i in range(N):
        d = Deikstra(i, Vlist2, N)
        distance.append(d)
    for U in range(len(distance)):
        for V, W in Vlist2[U]:
            distance[U][V] = distance[U][V] + h[V] - h[U]
    return distance

def spravka():
    print("**********************************************************************\n"
          "Автор работы: студент М3О-225Бк-21 Новиков К.А.\n"
          "Список ключей, доступных для ввода:\n"
          "    -e - ключ для ввода графа из файла, содержащего список ребер\n"
          "    -m - ключ для ввода графа из файла, содержащего матрицу смежности\n"
          "    -l - ключ для ввода графа из файла, содержащего список смежности\n"
          "Можно указать не более одного ключа для ввода графа!\n"
          "    -o - ключ для вывода результатов работы программы в файл res.txt\n"
          "    -h - ключ для вывода справки\n"
          "**********************************************************************")
