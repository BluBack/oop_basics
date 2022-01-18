class Inimene():
    def init(self, e_nimi="nimi", p_nimi="perenimi", arv="1"):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi


    def tutvusta(self):
        print("Tere, olen " + str(self.eesnimi) + " " + str(self.perenimi) + "!")

    def del(self):
        print("Kõike head, " + str(self.eesnimi) + ", " + str(self.perenimi) + "!")
