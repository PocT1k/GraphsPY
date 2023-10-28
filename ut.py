import math

from cl import *

MaxNumberV = 1000


# Эвристика Manhatten-метрики
# Оценивает расстояние между двумя точками как сумму абсолютных разниц по горизонтали и вертикали.
def hManhetten(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# Эвристика Чебышева
# Оценивает расстояние между двумя точками как максимальную абсолютную разницу по горизонтали и вертикали.
def hChebiseva(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return max(abs(x1 - x2), abs(y1 - y2))

# Евклидова эвристика
# Оценивает расстояние между двумя точками как геометрическое (евклидово) расстояние между ними.
def hEvklida(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Эвристика Дейкстры
# Фактически отсутствует, и стоимость всегда равна 0.
# Превращает алгоритм A* в алгоритм Дейкстры, который находит кратчайший путь, не учитывая эвристику.
def hDeikstra(a, b):
    return 0

def astar(map, Map1, start, end, h, Ni, Nj):
    # Создание начальной и конечной вершин с начальными значениями g, h и f
    start_node = Cell(None, start)
    start_node.g = 0  # Расстояние от начальной вершины до текущей
    start_node.h = 0  # Эвристика (оценка) расстояния от текущей вершины до конечной
    start_node.f = start_node.g + start_node.h  # Оценка общей стоимости (g + h)

    end_node = Cell(None, end)

    open_list = []  # Открытый список вершин
    closed_list = []  # Закрытый список вершин (уже обработанных)

    open_list.append(start_node)  # Начальную вершину добавляем в открытый список

    while open_list:
        current_node = open_list[0]  # Выбираем вершину с наименьшей оценкой f
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)  # Удаляем текущую вершину из открытого списка

        if current_node == end_node:  # Если текущая вершина - конечная, строим путь
            path = []
            total = current_node.g  # Длина найденного пути
            current = current_node
            k = (len(closed_list) * 100) / (Ni * Nj)  # Процент просмотренных клеток
            while current:
                path.append(current.position)
                current = current.parent
                if current == start_node:
                    break
            path.append(start_node.position)
            return path[::-1], total, k

        children = []

        # Генерируем потомков для текущей вершины
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Проверка, находятся ли потомки в пределах карты
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(map[len(map) - 1]) - 1) or node_position[1] < 0:
                continue

            new_node = Cell(current_node, node_position)  # Создаем потомка
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue
            k = child.position[0]
            l = child.position[1]
            i = current_node.position[0]
            j = current_node.position[1]

            # Вычисление предполагаемой стоимости для потомка
            tentative_g = current_node.g + abs(k - i) + abs(l - j) + abs(Map1.MD[k][l] - Map1.MD[i][j])

            if child not in open_list:
                # Если потомка нет в открытом списке (он еще не был рассмотрен)
                open_list.append(child)  # Добавляем потомка в открытый список
                tentative_is_better = True
            else:
                # Если потомок уже в открытом списке
                if tentative_g < child.g:
                    # Если новый путь до потомка короче, чем старый
                    tentative_is_better = True
                else:
                    tentative_is_better = False

            if tentative_is_better:
                # Если новый путь лучше (короче) или потомок еще не был в открытом списке
                child.parent = current_node  # Устанавливаем текущую вершину как родителя потомка
                child.g = tentative_g  # Обновляем стоимость пути до потомка

                # Выбор эвристики в зависимости от h
                if h == 1:
                    child.h = hManhetten(child.position, end_node.position)
                if h == 2:
                    child.h = hChebiseva(child.position, end_node.position)
                if h == 3:
                    child.h = hEvklida(child.position, end_node.position)
                if h == 4:
                    child.h = hDeikstra(child.position, end_node.position)

                child.f = child.g + child.h

    if current_node not in closed_list:
        closed_list.append(current_node)  # Добавляем текущую вершину в закрытый список
pass

def help():
    print("**********************************************************************\n"
          "Автор работы: студент М3О-225Бк-21 Новиков К.А.\n"
          "Список ключей, доступных для ввода:\n"
          "    -m map_file_path - ввод графа из матрицы смежности\n"
          "    -n begin_vertex_x begin_vertex_y - обязательная начальная вершина\n"
          "    -d end_vertex_x end_vertex_y - обязательная конечная вершина\n"
          "Можно указать не более одного ключа для ввода графа!\n"
          "    -o - ключ для вывода результатов работы программы в файл res.txt\n"
          "    -h - ключ для вывода справки\n"
          "**********************************************************************")
#help
