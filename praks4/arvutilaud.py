from praks4.kirjutuslaud import Kirjutuslaud

class Arvutilaud(Kirjutuslaud):
    def pindala(self, arvuti):
        return Kirjutuslaud.pindala(self) - arvuti