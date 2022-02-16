
class AknadUksed:
    """klass akna või ukse kirjeldamiseks"""
    def __init__(self, laius, kõrgus):
        """akna või ukse loomiseks vajalik konstruktor"""
        self.pindala = laius * kõrgus
        """aknale või uksele määratakse pindala"""
class Tuba:
    """klass toa kirjeldamiseks"""
    def __init__(self, p, l, k):
        """toa mõõtude lisamiseks vajalik konstruktor"""
        self.pikkus = p
        self.laius = l
        self.kõrgus = k
        self.aknad_uksed = []
    def lisaAkenUks(self, laius, kõrgus):
        self.aknad_uksed.append(AknadUksed(laius, kõrgus))
        """akna või ukse loomiseks vajalik konstruktor"""
    def täisPind(self):
        """täispinna loomiseks vajalik konstruktor"""
        return 2 + self.kõrgus * (self.pikkus + self.laius)
    def tööPind(self):
        """tööpinna loomiseks vajalik konstruktor """
        uus_pindala = self.täisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
            return uus_pindala
        """tapeedi kuluvuse arvutamine"""
    def tapeedid(self, tp, tl):
        """arvutame tapeedi pikkuse ja lajiuse"""
            return int(self.tööPind() / (tp * tl)) + 1