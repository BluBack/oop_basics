class Inimene():
    jk = 0
    def __init__(self):
        self.id = self.jk + 1
        self.jk += 1
    def info(self):
        print("id = " + str(self.id))