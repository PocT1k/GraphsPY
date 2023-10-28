class Map:
    def __init__(self, fname):
        Ni = 0
        Nj = 0
        MD = []
        fin = open(fname, "r")
        while (True):
            line = fin.readline().split()
            line = list(map(int, line))
            if not line:
                break
            MD.append(line)
            Nj = len(line)
            Ni += 1
        self.Ni = Ni
        self.Nj = Nj
        self.MD = MD
    def index(self, x, y):
        return self.MD[x][y]
    def neibhors(self, x, y):
        if x==0:
            if y==0:
                return [[x+1, y],[y+1, x]]
            if y==self.Nj:
                return [[x+1, y],[x, y-1]]
            else:
                return [[x, y-1],[x, y+1],[x+1, y]]
pass
