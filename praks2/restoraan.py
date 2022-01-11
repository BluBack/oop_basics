class Restoraan():
    restoraani_nimi = "nimi"
    soogi_tyyp = "söök"

    def kirjalda_restoraan(self):
        print("Restoraan " + str(self.restoraani_nimi) + " pakub " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")