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
print("Ruumi mõõdud on :")
p = float(input("Pikkus: "))
l = float(input("laius: "))
k = float(input("Kõrgus: "))

tuba = Tuba(p, l, k)

vastus = input("Kas toas on aknaid/uksi? jah/ei" )
while vastus == "jah":
    l = float(input("Akna/Ukse laius: "))
    k = float(input("Akna/Ukse kõrgus: "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas toas on aknaid/uksi? jah/ei" )

print("Tapeedid on vaja kleepida " + str(tuba.tööPind()) + " ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl)))
