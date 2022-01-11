class Kasutaja():
    first_name = ""
    surename = ""
    GPU = ""

    def tervita_kasutaja(self):
        print("Tere, " + str(self.first_name) + " " + str(self.surename))

    def kirjalda_Kasutaja(self):
        print("Kasutaja andmed: ")
        print("eesnimi: " str(self.first_name))
        print("eesnimi: " str(self.surename))

def kirjalda_Kasutaja_GPUd(self):
    print("kasutaja GPU on: "str(self.GPU))