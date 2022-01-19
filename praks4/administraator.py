from praks4.kasutaja import Kasutaja

class Admin(Kasutaja):
    privileegid = []
    def naita_privileegid(self):
        for jk in range(1, len(self.privileegid) + 1):
            print("{0}. {1}".format(jk, self.privileegid[jk - 1]))
    def maara_privileegid(self, valik):
            print("Lisa privileege: ")
            while (True):
                valik = input("Sisesta: ")
                if (valik == ""):
                    break
                self.privileegid.append(valik)