class AknadUksed:
    """klass akna või ukse kirjeldamiseks"""
    def __init__(self, laius, kõrgus):
        """akna või ukse loomiseks vajalik konstruktor"""
        self.pindala = laius * kõrgus
        """aknale või uksele määratakse pindala"""
class Tuba:
    """klass toa kirjeldamiseks"""
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.kõrgus = k
        self.aknad_uksed = []
    def lisaAkenUks(self, laius, kõrgus):
        self.aknad_uksed.append(AknadUksed(laius, kõrgus))
        """akna või ukse"""
    def täisPind(self):
        """täis pinna"""
        return 2 + self.kõrgus * (self.pikkus + self.laius)
    def tööPind(self):
        """tööpinna """
        uus_pindala = self.täisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
            return uus_pindala
    def tapeedid(self, tp, tl):
            return int(self.tööPind() / (tp * tl)) + 1
print("Ruumi mõõdud on :")
"""küsime kasutajalt vajalikud andmed"""
p = float(input("Pikkus: "))
l = float(input("laius: "))
k = float(input("Kõrgus: "))

tuba = Tuba(p, l, k)
"""loome toe objekti"""
vastus = input("Kas toas on aknaid/uksi? jah/ei" )
"""küsime kasutajalt kas toas on aknaid/uksi"""
while vastus == "jah":
    l = float(input("Akna/Ukse laius: "))
    k = float(input("Akna/Ukse kõrgus: "))
    """küsime vajalikud mõõdud"""
    aken_uks = AknadUksed(l, k)
    """loome akna või ukse objekti"""
    tuba.aknad_uksed.append(aken_uks)
    """lisame akna või ukse toa sisse"""
    vastus = input("Kas toas on aknaid/uksi? jah/ei" )
    """"""

print("Tapeedid on vaja kleepida " + str(tuba.tööPind()) + " ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl)))
"""küsime tapeedi rulli mõõdud"""
