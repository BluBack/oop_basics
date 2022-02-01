class Kasutaja():
    def __init__(self, e_nimi, p_nimi, su):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi
        self.sugu = su

    def kirjelda_kasutaja(self):
        print("Eesnimi: " + str(self.eesnimi) + ", Perenimi: " + str(self.perenimi) + ", Sugu: " + str(self.sugu))

    def tervita_kasutaja(self):
        print(str(self.eesnimi) + " " + str(self.perenimi) + ", Tere jälle!")
