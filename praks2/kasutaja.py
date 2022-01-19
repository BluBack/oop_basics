class Kasutaja():
    eesnimi = "Eesnimi"
    perenimi = "Perenimi"
    sugu = "Sugu"

    def kirjelda_kasutaja(self):
        print("Eesnimi: " + str(self.eesnimi) + ", Perenimi: " + str(self.perenimi) + ", Sugu: " + str(self.sugu))

    def tervita_kasutaja(self):
        print(str(self.eesnimi) + " " + str(self.perenimi) + ", Tere uuesti!")