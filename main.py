import sys

from ut import *
from mp import *


#-m map_001.txt -n 9 0 -d 3 9
if __name__ == "__main__":
    input_string = input("Введите данные: ") # Получаем входные данные от пользователя
    array = input_string.split()
    array.insert(0, "1")

    if len(array)<6: #Если не достаочно аргументов
        print("Ошибка! Нужно указать параметр -m, -n, -d, параметр -o, для вывода в файл или параметр -h, для вывода справки ")
        sys.exit(1)

    if "-h" in array:# Если есть аргумент -h, выводим справку и завершаем программу
        help()
        sys.exit(1)

    fname = array[2]
    parametr = array[1]

    # Создаем объект карты
    Map1 = Map(fname)
    Ni = Map1.Ni
    Nj = Map1.Nj

    # Получаем начальные и конечные координаты из аргументов
    Vsx = int(array[array.index("-n") + 1])
    Vsy = int(array[array.index("-n") + 2])
    Vex = int(array[array.index("-d") + 1])
    Vey = int(array[array.index("-d") + 2])
    Vs = (Vsx, Vsy)
    Ve = (Vex, Vey)

    # Выполняем поиск маршрута с разными эвристиками
    path, total, k = astar(Map1.MD, Map1, Vs, Ve, 1, Ni, Nj) # hManhetten
    print(path)
    print(f"Length = {total}, % = {k}")

    path, total, k = astar(Map1.MD, Map1, Vs, Ve, 2, Ni, Nj) # hChebiseva
    print(path)
    print(f"Length = {total}, % = {k}")

    path, total, k = astar(Map1.MD, Map1, Vs, Ve, 3, Ni, Nj) # hEvklida
    print(path)
    print(f"Length = {total}, % = {k}")

    path, total, k = astar(Map1.MD, Map1, Vs, Ve, 4, Ni, Nj) # hDeikstra
    print(path)
    print(f"Length = {total}, % = {k}")

pass
