class Kasutaja():
    first_name = ""
    surename = ""
    GPU = ""

    def tervita_kasutajat(self):
        print("Tere, " + str(self.first_name) + " " + str(self.surename))

    def kirjelda_Kasutaja(self):
        print("Kasutaja andmed: ")
        print("eesnimi: " str(self.first_name))
        print("eesnimi: " str(self.surename))

def kirjelda_Kasutaja_GPUd(self):
    print("kasutaja GPU on: "str(self.GPU))