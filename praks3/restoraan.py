class Restoraan():
    def __init__(self, restorani_nimi, söögi_tyyp):
        self.restorani_nimi = restorani_nimi
        self.söögi_tyyp = söögi_tyyp

    def kirjalda_restoraan(self):
        print("Restoraan " + str(self.restorani_nimi) + " pakub " + str(self.söögi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")