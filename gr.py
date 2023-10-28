class Graph: #основной класс ?рафа
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
