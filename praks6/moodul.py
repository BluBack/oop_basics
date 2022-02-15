class AknadUksed:
    def __init__(self, laius, kõrgus):
        self.pindala = laius * kõrgus
class Tuba:
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.kõrgus = k
        self.aknad_uksed = []
    def lisaAkenUks(self, laius, kõrgus):
        self.aknad_uksed.append(AknadUksed(laius, kõrgus))
    def täisPind(self):
        return 2 + self.kõrgus * (self.pikkus + self.laius)
    def tööPind(self):
        uus_pindala = self.täisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
            return uus_pindala
        def tapeedid(self, tp, tl):
            return int(self.tööPind() / (tp * tl)) + 1