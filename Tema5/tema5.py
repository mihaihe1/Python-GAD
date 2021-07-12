class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        rez_numarator = self.numarator * other.numitor + self.numitor * other.numarator
        rez_numitor = self.numitor * other.numitor
        div = Fractie.cmmdc(rez_numarator, rez_numitor)
        return Fractie(rez_numarator // div, rez_numitor // div)

    def __sub__(self, other):
        rez_numarator = self.numarator * other.numitor - self.numitor * other.numarator
        rez_numitor = self.numitor * other.numitor
        div = Fractie.cmmdc(rez_numarator, rez_numitor)
        return Fractie(rez_numarator // div, rez_numitor // div)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

    @staticmethod
    def cmmdc(x, y):
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x

        return x


f1 = Fractie(2, 3)
f2 = Fractie(1, 3)
print(f1.inverse() + f2)

