MaxNumberV = 1000


"""BFS O(|v|+|e|)"""


def BFS(Vlist, V0list):
    KS = []
    visited = set()
    for V0 in V0list:
        if V0 in visited:
            continue
        queue = []
        currKS = []
        visited.add(V0)
        queue.append(V0)
        while queue:
            V = queue.pop(0)
            currKS.append(V + 1)
            for Vertex in Vlist[V]:
                if Vertex not in visited:
                    visited.add(Vertex)
                    queue.append(Vertex)
        currKS.sort()
        KS.append(currKS)
    return KS


"""DFS O(|v|+|e|)"""


def DFS(Vlist, V0list):
    visited = set()
    KS = []
    K = 0
    M = [0] * len(V0list)
    for V0 in V0list:
        if V0 not in visited:
            currKS = []
            stack = []
            stack.append(V0)
            visited.add(V0)
            currKS.append(V0 + 1)
            K += 1
            M[V0] = K
            while stack:
                V = stack.pop()
                K += 1
                M[V] = K
                for Vertex in Vlist[V]:
                    if Vertex not in visited:
                        stack.append(V)
                        visited.add(Vertex)
                        currKS.append(Vertex + 1)
                        stack.append(Vertex)
                        break
            currKS.sort()
            KS.append(currKS)
    return KS, M


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
