class Ristkylik():
    def __init__(self, laius, korgus, symbol):
        self.laius = l
        self.korgus = k
        self.symbol = s

    def __str__(self):
        ruut = []
        for rea_number in range(self.korgus):
            rida = self.symbol * self.laius
            ruut.append(rida)
        ruut = "\n".join(ruut)
        return ruut

    def __add__(self, other):
        self.laius = self.laius + other.laius
        self.korgus = self.korgus + other.korgus
        symboli_valik = random.randint(1, 2)

        if symboli_valik == 1:
            self.symbol = self.symbol
        else:
            self.symbol = other.symbol
        return self