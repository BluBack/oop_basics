class Konto:
    def init(self, nimi, saldo):
        self.nimi = nimi
        self.raha = saldo

    def ylekanne(self, kogus):
        summa = self.raha - kogus
        print("Te tegite ülekande suurusega " + str(summa))

    def deposiit(self, kogus):
       summa = self.raha + kogus
       print("Te depositisite " + str(summa))

    def naita_saldo(self):
        return str(self.raha) + " eurot"

    def naita_nimi(self):
        print("Teie nimi on: " + str(self.nimi))