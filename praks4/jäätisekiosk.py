from praks4.restoraan import Restoraan

class jäätisekiosk(Restoraan):
    jaatise_valik = []

    def naita_jaatise_valik(self):
        for jk in range(1, len(self.naita_jaatise_valik) + 1):
            print("{0}. {1}".format(jk, self.jaatise_valik [jk-1]))

    def maara_jaatise_valik(self, valik):
        self.jaatise_valik = valik
        print("Lisa jäätise variandid: ")
        while(True):
            valik = input("Sisesta: ")
            self.jaatise_valik.append(valik)
            if(valik == ""):
                break
            self.jaatise_valik.append(valik)